#!/usr/bin/env python3
"""Copy the website photos from DRIVE-IMAGES into media/drive/, resized.
drive_map.tsv lists: Drive file id <TAB> Drive folder <TAB> file name.
Writes drive_map.json (id -> media path) used by build.py. Safe to re-run.
Each photo gets a full version (1800px) and a small one (*.sm.jpg, 900px) for grids.
Animated GIFs become a looping MP4 plus a poster frame (much lighter than GIF)."""
import json, os, re, subprocess, sys, pathlib
from PIL import Image, ImageOps, ImageSequence
Image.MAX_IMAGE_PIXELS = None
HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parent
DRIVE = SITE.parent / "DRIVE-IMAGES"
ALIAS = {"INVERSE": "INVERSE_SURVEILLANCE"}

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def find(folder, name):
    folder = ALIAS.get(folder, folder)
    p = DRIVE / folder / name
    if p.exists():
        return p
    top = DRIVE / folder.split("/")[0]
    for base in (DRIVE / folder, top, DRIVE):
        if base.exists():
            for q in base.rglob("*"):
                if q.name.lower() == name.lower():
                    return q
    return None

def small_of(p):
    return p.with_name(p.stem + ".sm.jpg")

out_map, missing = {}, []
jpath = HERE / "drive_map.json"
if jpath.exists():
    out_map = json.loads(jpath.read_text())
for line in (HERE / "drive_map.tsv").read_text().splitlines():
    fid, folder, name = line.split("\t")
    rel = out_map.get(fid)
    if rel and rel.endswith(".gif"):
        rel = None  # re-do GIFs as video
    if rel and (SITE / "media" / rel).exists() and small_of(SITE / "media" / rel).exists():
        continue
    src = find(folder, name)
    if not src:
        missing.append(f"{folder}/{name}"); continue
    base = f"drive/{slug(folder)}/{slug(pathlib.Path(name).stem)}"
    if src.suffix.lower() == ".gif":
        rel = base + ".mp4"
        dst = SITE / "media" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf",
                        "scale='min(1280,iw)':-2,fps=20", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                        "-crf", "27", "-movflags", "+faststart", "-an", str(dst)], check=True)
        im = Image.open(src).convert("RGB")
        poster = dst.with_suffix(".jpg")
        im.thumbnail((1800, 1800)); im.save(poster, "JPEG", quality=80, optimize=True, progressive=True)
        im.thumbnail((900, 900)); im.save(small_of(dst), "JPEG", quality=76, optimize=True, progressive=True)
    else:
        rel = base + ".jpg"
        dst = SITE / "media" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            im = Image.open(dst)
        else:
            im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
            im.thumbnail((1800, 1800), Image.LANCZOS)
            im.save(dst, "JPEG", quality=80, optimize=True, progressive=True)
        sm = im.copy(); sm.thumbnail((900, 900), Image.LANCZOS)
        sm.save(small_of(dst), "JPEG", quality=76, optimize=True, progressive=True)
    out_map[fid] = rel
    jpath.write_text(json.dumps(out_map, indent=0))
    print("ok", rel, dst.stat().st_size // 1024, "KB", flush=True)
jpath.write_text(json.dumps(out_map, indent=0))
print("done", len(out_map), "missing", missing)
