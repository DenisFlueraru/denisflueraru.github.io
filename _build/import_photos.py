#!/usr/bin/env python3
"""Import a folder of photos and videos from DRIVE-IMAGES into media/, ready for content.py.

    python3 _build/import_photos.py "WORKSHOPS/Libra Bank" workshops/libra

Add --force at the end to redo files that were already imported (after you have
replaced or re-cropped one of the originals, say).

The first argument is a folder inside DRIVE-IMAGES; the second is the name the
photos get inside media/ (folder/prefix). Each photo is written twice — a full
version capped at 1800px and a .sm.jpg at 900px that the grids use — and the
lines to paste into content.py are printed at the end.

Photos are taken in filename order, so name them Libra1, Libra2, Libra3 if the
order matters. Re-running is safe: files already imported are left alone.

A video in the same folder (.mov, .mp4, .m4v, .avi) is re-encoded to H.264 MP4 with
its sound kept, so every browser can play it, plus a poster frame. Phone videos are
often HEVC, which Safari plays and most other browsers do not — this fixes that.
"""
import pathlib
import subprocess
import sys
from PIL import Image, ImageOps

Image.MAX_IMAGE_PIXELS = None
HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parent
# the photos live next to the site: ../DRIVE-IMAGES from site-v2, or
# ../DENISFLUERARU.COM/DRIVE-IMAGES from the GitHub repo folder
DRIVE = next((d for d in (SITE.parent / "DRIVE-IMAGES", SITE.parent / "DENISFLUERARU.COM" / "DRIVE-IMAGES")
              if d.is_dir()), SITE.parent / "DRIVE-IMAGES")
FULL, SMALL, Q = 1800, 900, 80
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".heic"}
VID_EXTS = {".mov", ".mp4", ".m4v", ".avi", ".mkv"}
VID_W = 1280


def main():
    args = [a for a in sys.argv[1:] if a != "--force"]
    force = "--force" in sys.argv
    if len(args) != 2:
        print(__doc__)
        return 2

    folder, prefix = args[0], args[1].strip("/")
    src_dir = DRIVE / folder
    if not src_dir.is_dir():
        print(f"No such folder: {src_dir}")
        print("Folders available in DRIVE-IMAGES:")
        for d in sorted(p for p in DRIVE.rglob("*") if p.is_dir()):
            print("   ", d.relative_to(DRIVE))
        return 1

    files = [p for p in sorted(src_dir.iterdir()) if p.is_file() and not p.name.startswith(".")]
    photos = [p for p in files if p.suffix.lower() in EXTS]
    videos = [p for p in files if p.suffix.lower() in VID_EXTS]
    if not photos and not videos:
        print(f"Nothing to import in {src_dir}")
        return 1

    out_dir = SITE / "media" / pathlib.PurePosixPath(prefix).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = pathlib.PurePosixPath(prefix).name

    refs = []
    for i, p in enumerate(photos, 1):
        rel = f"{pathlib.PurePosixPath(prefix).parent}/{stem}-{i}.jpg"
        dst = SITE / "media" / rel
        small = dst.with_name(dst.stem + ".sm.jpg")
        refs.append(rel)
        if dst.exists() and small.exists() and not force:
            print(f"  skip  {rel}  (already imported — use --force to redo)")
            continue
        im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
        big = im.copy()
        big.thumbnail((FULL, FULL), Image.LANCZOS)
        big.save(dst, "JPEG", quality=Q, optimize=True, progressive=True)
        sm = im.copy()
        sm.thumbnail((SMALL, SMALL), Image.LANCZOS)
        sm.save(small, "JPEG", quality=76, optimize=True, progressive=True)
        print(f"  ok    {rel}  {dst.stat().st_size // 1024} KB   <- {p.name}")

    clips = []
    for i, v in enumerate(videos, 1):
        suffix = "-clip" if len(videos) == 1 else f"-clip-{i}"
        rel = f"{pathlib.PurePosixPath(prefix).parent}/{stem}{suffix}.mp4"
        dst = SITE / "media" / rel
        poster = dst.with_suffix(".jpg")
        clips.append(rel)
        if dst.exists() and poster.exists() and not force:
            print(f"  skip  {rel}  (already imported — use --force to redo)")
            continue
        print(f"  ...   {rel}  (re-encoding {v.name}, this takes a moment)", flush=True)
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(v),
            # cap the LONG edge, so portrait phone clips come out portrait and small
            "-vf", (f"scale=w='min({VID_W},iw)':h='min({VID_W},ih)'"
                    f":force_original_aspect_ratio=decrease:force_divisible_by=2:flags=lanczos"),
            "-c:v", "libx264", "-preset", "slow", "-crf", "23", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(dst)], check=True)
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(dst),
            "-ss", "0.5", "-frames:v", "1", "-q:v", "4", str(poster)], check=True)
        print(f"  ok    {rel}  {dst.stat().st_size // 1024} KB   <- {v.name}")

    print("\nPaste these into the entry in _build/content.py:\n")
    if refs:
        print(f'         main="{refs[0]}",')
    if len(clips) == 1:
        print(f'         clip="{clips[0]}",')
    elif clips:
        inner = ", ".join(f'"{c}"' for c in clips)
        print(f"         clips=[{inner}],")
    if len(refs) > 1:
        inner = ", ".join(f'"{r}"' for r in refs[1:])
        print(f"         grid=[{inner}]),")
    print("\nThen run:  python3 _build/build.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
