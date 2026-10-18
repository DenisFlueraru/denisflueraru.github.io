#!/usr/bin/env python3
"""Builds the portfolio into ../out. Run: python3 build.py"""
import html, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content import ARTWORKS, WORKSHOPS, COLLABS, EXHIBITIONS, INDEX, SERVICES, CATS, HB_TEXT

OUT = pathlib.Path(__file__).parent.parent
E = html.escape
SITE = "Denis Flueraru"
LOGO = "lh3:1Oz-mWMgJsv7vnKWHDUaHM4pgjF8NZavd"
NAV = [("artworks.html", "Artworks"), ("workshops.html", "Workshops"), ("sound.html", "Sound"),
       ("collabs.html", "Collabs"), ("exhibitions.html", "Exhibitions"), ("services.html", "Services")]
NAV_END = [("biography.html", "Bio"), ("contact.html", "Contact")]
SOCIAL = [("Instagram", "https://www.instagram.com/denisflueraru/"),
          ("LinkedIn", "https://www.linkedin.com/in/denisflueraru/"),
          ("YouTube", "https://www.youtube.com/@atomatlab"),
          ("SoundCloud", "https://soundcloud.com/leselmusic"),
          ("ATOMAT LAB ↗", "https://atomatlab.com")]
CV_URL = "media/Denis_Flueraru_CV.pdf"


import json
_MAP_FILE = pathlib.Path(__file__).parent / "drive_map.json"
DRIVE = json.loads(_MAP_FILE.read_text()) if _MAP_FILE.exists() else {}
DOMAIN = "https://denisflueraru.com/"


def local(ref):
    """Resolve an image ref to a media/ path if we have a local copy, else None."""
    if ref.startswith("lh3:"):
        rel = DRIVE.get(ref[4:])
        return rel and f"media/{rel}"
    return f"media/{ref}"


def src(ref, w=1600):
    path = local(ref)
    if path is None:
        return f"https://lh3.googleusercontent.com/d/{ref[4:]}=w{w}"
    if path.endswith(".mp4"):
        path = path[:-4] + ".jpg"
    if w <= 1200:
        small = path[:-4] + ".sm.jpg"
        if (OUT / small).exists():
            path = small
    return path


def frame(ref, label, cls="", zoom=True, eager=False, alt=None, w=1600):
    alt = label if alt is None else alt
    path = local(ref)
    if path and path.endswith(".mp4"):
        return (f'<figure class="frame {cls}" data-label="{E(label)}"><video src="{path}" poster="{src(ref, w)}" '
                f'autoplay muted loop playsinline preload="metadata" aria-label="{E(alt)}"></video></figure>')
    z = ' data-zoom tabindex="0" role="button" aria-label="Enlarge image: ' + E(alt) + '"' if zoom else ""
    full = f' data-full="{src(ref, 2400)}"' if zoom else ""
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<figure class="frame {cls}" data-label="{E(label)}"{z}>'
            f'<img src="{src(ref, w)}"{full} alt="{E(alt)}" {loading} decoding="async" referrerpolicy="no-referrer"></figure>')


def dot(cat):
    return f'<span class="dot {cat}" aria-hidden="true"></span>'


def page(fname, title, desc, body, current=None, og_img=None):
    cur = lambda h: ' aria-current="page"' if h == current else ""
    nav = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in NAV)
    nav_end = (f'<a class="shop-link" href="https://atomatlab.com" target="_blank" rel="noopener">{dot("col")}Shop ↗</a>'
               + "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in NAV_END))
    menu_links = "".join(f'<a href="{h}">{t}<span>{i+1:02d}</span></a>' for i, (h, t) in enumerate(NAV + NAV_END))
    menu_links += f'<a href="https://atomatlab.com" target="_blank" rel="noopener">Shop ↗<span>ATOMAT LAB</span></a>'
    social = "".join(f'<a class="mono" href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in SOCIAL)
    full_title = f"{title} — {SITE}" if title != SITE else f"{SITE} — an archive of ongoing experiments"
    og_src = src(og_img, 1600) if og_img else ""
    og = f'\n<meta property="og:image" content="{og_src if og_src.startswith("http") else DOMAIN + og_src}">' if og_img else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="website">{og}
<meta name="theme-color" content="#cfcec9">
<link rel="icon" type="image/png" href="media/atomatfavicon.png">
<link rel="canonical" href="{DOMAIN}{"" if fname == "index.html" else fname}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;800&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
<script src="assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <div class="bar">
      <a class="brand" href="index.html">Denis Flueraru</a>
      <nav class="nav" aria-label="Main">{nav}</nav>
      <nav class="nav nav-end" aria-label="Secondary">{nav_end}</nav>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
    </div>
  </div>
</header>
<div class="menu-panel" id="menu" hidden>
  <div class="bar"><a class="brand" href="index.html">Denis Flueraru</a><button class="menu-btn menu-close" type="button" style="display:inline-flex">Close</button></div>
  <nav aria-label="Menu">{menu_links}</nav>
  <div class="foot">{social}</div>
</div>
<main id="main">
{body}
</main>
<footer class="wrap">
  <div class="grid12 site-foot">
    <a class="mail" href="mailto:flueraru.denis@gmail.com">flueraru.denis@gmail.com</a>
    <div class="links">{social}<a class="mono" href="{CV_URL}" target="_blank" rel="noopener">CV (PDF) ↓</a></div>
    <div class="legal mono muted"><span>© Denis Flueraru — Bucharest, RO</span><span>sound · form · code</span></div>
  </div>
</footer>
<a class="spin" href="https://atomatlab.com" target="_blank" rel="noopener" aria-label="ATOMAT LAB shop">
  <img src="media/atomatlabrotating.png" data-alt="media/field5.png" alt="" referrerpolicy="no-referrer">
</a>
<div class="lb" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="Image viewer">
  <div class="top"><span class="lb-count"></span><button class="lb-close" type="button">Close ✕</button></div>
  <div style="display:flex;min-height:0"><img alt=""></div>
  <div class="bot"><button class="lb-prev" type="button" aria-label="Previous image">←</button><button class="lb-next" type="button" aria-label="Next image">→</button></div>
</div>
</body>
</html>
"""


def page_head(title, side="", crumbs=None, h1_extra=""):
    cr = ""
    if crumbs:
        cr = '<nav class="crumbs mono" aria-label="Breadcrumb">' + " <span>/</span> ".join(
            f'<a href="{h}">{E(t)}</a>' if h else f"<span>{E(t)}</span>" for h, t in crumbs) + "</nav>"
    return f"""<div class="wrap">{cr}
  <section class="grid12 page-head">
    <h1 class="rise"{h1_extra}>{title}</h1>
    <div class="side mono rise d1">{side}</div>
  </section>
</div>"""


def write(name, content):
    (OUT / name).write_text(content, encoding="utf-8")


# ------------------------------------------------------------------ home
def build_index():
    legend = "".join(f'<span class="cat">{dot(k)}{n}s</span>' if k != "snd" else f'<span class="cat">{dot(k)}Sound &amp; instruments</span>'
                     for k, (n, _) in CATS.items())
    filters = '<button type="button" data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" data-filter="{k}" aria-pressed="false">{dot(k)}{("Sound" if k == "snd" else n + "s")}</button>'
        for k, (n, _) in CATS.items())
    rows = []
    for i, (t, y, c, p, href) in enumerate(INDEX, 1):
        ext = href.startswith("http")
        new = ' <span class="tag-new">NEW</span>' if t == "Heartbroken" else ""
        label = CATS[c][0]
        inner = (f'<span class="n mono">{i:03d}</span><span class="t">{E(t)}{new}</span>'
                 f'<span class="y mono">{y}</span><span class="cat mono">{dot(c)}{label}</span>'
                 f'<span class="p mono muted">{E(p)}{" ↗" if ext else ""}</span>')
        attrs = ' target="_blank" rel="noopener"' if ext else ""
        rows.append(f'<li class="row" data-cat="{c}"><a href="{href}"{attrs}>{inner}</a></li>')
    hb = ARTWORKS[0]
    tiles = "".join(
        f'<a class="tile" href="{a["slug"]}.html">{frame(a["hero"], a["title"], zoom=False, w=1000)}'
        f'<span class="cap"><strong>{E(a["title"])}</strong><span class="mono">{a["year"]}</span></span></a>'
        for a in [ARTWORKS[i] for i in (7, 3, 1)])
    body = f"""<div class="wrap">
  <section class="grid12 hero">
    <h1 class="rise">an archive of ongoing <span class="hl">experiments</span></h1>
    <div class="hero-side mono rise d1">
      <p>Creative technologist working across sound, form and code — installations, instruments, workshops. Bucharest, RO.</p>
      <div class="legend">{legend}</div>
    </div>
  </section>

  <section class="grid12 featured" aria-labelledby="feat-title">
    <a class="lead pair" href="heartbroken.html" aria-label="Heartbroken — view project">{"".join(frame(r, "Heartbroken", zoom=False, eager=True, w=1000) for r in hb["pair"])}</a>
    <div class="copy">
      <div style="display:flex;flex-direction:column;gap:20px">
        <div class="eyebrow mono"><span class="tag-new">NEW</span><span>Collab — 2026</span></div>
        <h2 id="feat-title">Heartbroken</h2>
        <p>{E(HB_TEXT[0])}</p>
      </div>
      <dl class="facts"><dt>Concept</dt><dd>Michelle Bressan</dd><dt>Design &amp; production</dt><dd>Denis Flueraru</dd><dt>Materials</dt><dd>Stethoscope, amplifier, distortion pedal, speaker</dd><dt>Year</dt><dd>2026</dd></dl>
      <a class="link-arrow mono" href="heartbroken.html">View project →</a>
    </div>
  </section>

  <section class="index" aria-labelledby="idx-title">
    <div class="section-head">
      <h2 id="idx-title">Index <span class="count"></span></h2>
      <div class="filters" role="group" aria-label="Filter the index">{filters}</div>
    </div>
    <ol class="rows">{"".join(rows)}</ol>
  </section>

  <section aria-label="Selected artworks">
    <div class="tiles">{tiles}</div>
    <a class="link-arrow mono" href="artworks.html">All artworks →</a>
  </section>
</div>"""
    write("index.html", page("index.html", SITE,
        "Denis Flueraru — creative technologist in Bucharest. Interactive installations, sound art, custom instruments and workshops.",
        body, og_img="heartbroken/heartbroken-4.jpg"))


# ------------------------------------------------------------------ artworks
def build_artworks():
    tiles = "".join(
        f'<a class="tile" href="{a["slug"]}.html">{frame(a["hero"], a["title"], zoom=False, w=1000, eager=i < 3)}'
        f'<span class="cap"><strong>{E(a["title"])}{" <span class=tag-new>NEW</span>" if a.get("new") else ""}</strong>'
        f'<span class="mono">{a["year"]}</span></span></a>'
        for i, a in enumerate(ARTWORKS))
    body = page_head("Artworks", f"<p>{len(ARTWORKS)} works, 2022 — 2026.</p><p>Installations, sound objects and series.</p>") + \
        f'<div class="wrap"><section class="tiles">{tiles}</section></div>'
    write("artworks.html", page("artworks.html", "Artworks",
        "Artworks by Denis Flueraru — interactive installations, sound objects and series, 2022–2026.", body, current="artworks.html"))


def jpeg_size(path):
    """Width and height of a JPEG, without needing PIL at build time."""
    try:
        with open(path, "rb") as f:
            if f.read(2) != b"\xff\xd8":
                return None
            while True:
                b = f.read(1)
                while b and b != b"\xff":
                    b = f.read(1)
                marker = f.read(1)
                while marker == b"\xff":
                    marker = f.read(1)
                if not marker:
                    return None
                if marker[0] in (0xD8, 0xD9) or 0xD0 <= marker[0] <= 0xD7:
                    continue
                length = int.from_bytes(f.read(2), "big")
                if marker[0] in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                                 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    f.read(1)
                    h = int.from_bytes(f.read(2), "big")
                    w = int.from_bytes(f.read(2), "big")
                    return w, h
                f.read(length - 2)
    except OSError:
        return None


def clip_player(ref, title, cls="video"):
    """A local video file with controls and sound — imported by _build/import_photos.py.
    Nothing downloads until the visitor presses play. The box takes the clip's own
    shape, read off the poster frame, so a phone video stays portrait."""
    path = local(ref)
    poster = path[:-4] + ".jpg"
    size = jpeg_size(OUT / poster)
    shape, style = "", ""
    if size:
        w, h = size
        style = f' style="aspect-ratio: {w} / {h}"'
        if h > w:
            shape = " portrait"
    return (f'<figure class="frame contain {cls} clip{shape}" data-label="{E(title)}"{style}>'
            f'<video src="{path}" poster="{poster}" controls playsinline preload="none" '
            f'aria-label="{E(title)} — video"></video></figure>')


def yt_player(vid, title, cls="video"):
    """Click-to-play YouTube: shows the thumbnail, loads the player only on click.
    Works when opened from disk too (falls back to opening YouTube)."""
    return (f'<div class="{cls} yt"><a class="yt-btn" href="https://www.youtube.com/watch?v={vid}" '
            f'target="_blank" rel="noopener" data-yt="{vid}" aria-label="Play video: {E(title)}">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy">'
            f'<span class="yt-play mono">▶ Play</span></a></div>')


def embed_html(kind, ident, label, link):
    if kind == "youtube":
        return f'<div class="embed"><span class="mono">{E(label)}</span>{yt_player(ident, label)}</div>'
    if kind == "short":
        return f'<div class="embed"><span class="mono">{E(label)}</span>{yt_player(ident, label, "short")}</div>'
    if kind == "bandcamp":
        return (f'<div class="embed bc"><span class="mono">{E(label)}</span>'
                f'<iframe src="https://bandcamp.com/EmbeddedPlayer/album={ident}/size=large/bgcol=ffffff/linkcol=151515/tracklist=false/transparent=true/" '
                f'title="{E(label)}" loading="lazy" seamless><a href="{link}">{E(label)}</a></iframe></div>')
    return ""


def hero_html(a):
    if a.get("pair"):
        return '<div class="proj-hero pair">' + "".join(
            frame(r, a["title"], eager=True, alt=f'{a["title"]}, view {k+1}', w=1200) for k, r in enumerate(a["pair"])) + "</div>"
    return frame(a["hero"], a["title"], cls="proj-hero", eager=True, alt=a["title"])


def build_projects():
    n = len(ARTWORKS)
    for i, a in enumerate(ARTWORKS):
        prev_a, next_a = ARTWORKS[(i - 1) % n], ARTWORKS[(i + 1) % n]
        facts = "".join(f"<dt>{E(k)}</dt><dd>{E(v)}</dd>" for k, v in a["facts"])
        text = "".join(f"<p>{E(p)}</p>" for p in a["text"])
        side = (f'<div class="eyebrow">{"<span class=tag-new>NEW</span>" if a.get("new") else ""}'
                f'<span class="cat">{dot("art")}Artwork — {a["year"]}</span></div>')
        gal = ""
        if a.get("gallery"):
            cls = "gallery portrait" if a.get("portrait") else ("gallery two" if len(a["gallery"]) in (2, 4) else "gallery")
            gal = f'<section class="{cls}" data-gallery>' + "".join(
                frame(g, f'{a["title"]} — image {k+1}', alt=f'{a["title"]}, view {k+1}', w=1200) for k, g in enumerate(a["gallery"])) + "</section>"
        for title, imgs in a.get("sections", []):
            gal += f'<h2 class="sub-head">{E(title)}</h2><section class="gallery two" data-gallery>' + "".join(
                frame(g, f'{a["title"]} — {title}', alt=f'{a["title"]}, {title}', w=1200) for g in imgs) + "</section>"
        emb = ""
        if a.get("embeds"):
            emb = '<section class="embeds">' + "".join(embed_html(*e) for e in a["embeds"]) + "</section>"
        body = page_head(E(a["title"]), side, crumbs=[("artworks.html", "Artworks"), (None, f"{i+1:03d}")]) + f"""
<div class="wrap">
  <div data-gallery>
    {hero_html(a)}
    <section class="grid12 proj-body">
      <dl class="facts">{facts}</dl>
      <div class="text">{text}</div>
    </section>
    {gal}
  </div>
  {emb}
  <nav class="prevnext mono" aria-label="More artworks">
    <a href="{prev_a["slug"]}.html"><span>← Previous</span><strong>{E(prev_a["title"])}</strong></a>
    <a href="{next_a["slug"]}.html"><span>Next →</span><strong>{E(next_a["title"])}</strong></a>
  </nav>
</div>"""
        desc = a["text"][0][:155].rsplit(" ", 1)[0] + "…" if len(a["text"][0]) > 155 else a["text"][0]
        write(f'{a["slug"]}.html', page(f'{a["slug"]}.html', f'{a["title"]} ({a["year"]})', desc, body,
                                        current="artworks.html", og_img=a["hero"]))


# ------------------------------------------------------------------ entries
def entry(e, cat, label, ex=False):
    meta_extra = "".join(f'<span class="mono muted">{E(d)}</span>' for d in e.get("dates", [])) if ex else \
        f'<span class="mono muted">{E(e["place"])}</span>'
    text = f'<p>{E(e["text"])}</p>' if e.get("text") else ""
    media = ""
    clips = ""
    if e.get("clip"):
        clips += clip_player(e["clip"], e["title"])
    if e.get("clips"):
        # several clips sit side by side in one full-width row
        clips += '<div class="clips">' + "".join(clip_player(c, e["title"]) for c in e["clips"]) + "</div>"
    imgs = e.get("grid", []) if not ex else ["lh3:" + x for x in e["imgs"]]
    if e.get("portrait"):
        # all-portrait shoots: photos in one row at their own 3:4 shape, clips underneath
        imgs = ([e["main"]] if e.get("main") else []) + imgs
        media += "".join(frame(g, f'{e["title"]} — {k+1}', cls="tall", w=900) for k, g in enumerate(imgs)) + clips
    else:
        if e.get("main"):
            media += frame(e["main"], e["title"], cls="main", w=1600)
        media += clips
        if e.get("video"):
            media += yt_player(e["video"], e["title"])
        media += "".join(frame(g, f'{e["title"]} — {k+1}', w=900) for k, g in enumerate(imgs))
    gcls = {2: " g2", 3: " g3"}.get(len(imgs), "")
    return f"""<article class="grid12 entry{' ex' if ex else ''}" id="{e["id"]}">
  <div class="meta">
    <span class="cat mono">{dot(cat)}{label} — {e["year"]}</span>
    <h2>{E(e["title"])}</h2>
    {meta_extra}
    {text}
  </div>
  <div class="media{gcls}" data-gallery>{media}</div>
</article>"""


def build_entries():
    body = page_head("Workshops", "<p>Hands-on sessions: microphones, sensors, circuits and collective composition.</p>") + \
        '<div class="wrap">' + "".join(entry(w, "ws", "Workshop") for w in WORKSHOPS) + "</div>"
    write("workshops.html", page("workshops.html", "Workshops",
        "Workshops by Denis Flueraru — contact microphones, EMF microphones, sensors and collective composition.", body, current="workshops.html"))

    body = page_head("Collabs", "<p>Commissions, productions and collaborations — sound design, LED, sensors, bespoke instruments.</p>") + \
        '<div class="wrap">' + "".join(entry(c, "col", "Collab") for c in COLLABS) + "</div>"
    write("collabs.html", page("collabs.html", "Collabs",
        "Collaborations and commissions — sound design, LED programming, sensor systems and bespoke instruments.", body, current="collabs.html"))

    body = page_head("Exhibitions", "<p>Group and solo shows, 2023 — 2025.</p>") + \
        '<div class="wrap">' + "".join(entry(x, "ex", "Exhibition", ex=True) for x in EXHIBITIONS) + "</div>"
    write("exhibitions.html", page("exhibitions.html", "Exhibitions",
        "Exhibitions featuring Denis Flueraru's work in Bucharest, Brașov, Budapest and beyond.", body, current="exhibitions.html"))


# ------------------------------------------------------------------ sound
def yt(i, t):
    return yt_player(i, t)


def build_sound():
    instruments = ["1XQTM3Nd1_NKLke8pHa1QQ1ngooN0MQ5w", "1G7Qc3_bLRRI7ZDTGr70UnyRfv0YoUQSK", "1GOh7p34o8NbTMgKFLa-fTJGu1bqWr0rW",
                   "1cwQNX0KgOlMMv5qdjhWIq9tRVptcPKiA", "1yCQaTTTwz6vQW0v2uVro-gEqY5B1-xLD", "19xs2nu2QZFcXYRTaG0g6HXVygaUYU7C4"]
    performances = ["1VvmRTEU6_i7G1xzGDGP2oKZYkODqkf59", "1wuoe6s33QoghAYqXNZW-zNE0Cm8ApoVj", "1DOxb_KPaSpo-8MZoQ9TWI2XOC8c_8Tyq",
                    "1NXZFUZNo-VFMpDvq-ctkrGG6IDBVM3DU", "1tq3_TthrP_ZJakFxDQivtpvuP8Nelunv"]
    lesel = [
        yt("NhUxxw2keDg", "LESEL"), yt("NWbQPO3mKYA", "LESEL"),
        frame("sound/lesel1.jpg", "LESEL", w=900), yt("OCOhSMA0k8c", "LESEL"), yt("x_3DH34416c", "LESEL"),
        frame("sound/lesel2.jpg", "LESEL", w=900), frame("sound/lesel3.jpg", "LESEL", w=900),
        yt("qRL7gapq0E4", "LESEL"), yt("HgaK4oZQBrc", "LESEL"), frame("sound/lesel4.jpg", "LESEL", w=900),
    ]
    body = page_head("Sound", "<p>Aliases, custom instruments, performances and releases.</p>") + f"""
<div class="wrap">
  <article class="grid12 entry" id="instruments">
    <div class="meta">
      <span class="cat mono">{dot("snd")}Instruments &amp; performances</span>
      <h2>Custom instruments</h2>
      <p>I build bespoke microphones to record in specific environments — more at <a class="link-arrow" href="https://atomatlab.com" target="_blank" rel="noopener">atomatlab.com ↗</a></p>
      <p>My sound work has been presented at Sound Campus – Open Stream, Linz (AT), where Ruined Resonances was performed throughout Ars Electronica, and at RADAR 2023, Bucharest (RO), where I performed Sonic Imprints — an interactive audio-visual performance transcribing frequencies with a pen plotter.</p>
    </div>
    <div class="media" data-gallery>
      {"".join(frame("lh3:" + x, "Instruments", w=900) for x in instruments)}
      {"".join(frame("lh3:" + x, "Performances", w=900) for x in performances)}
    </div>
  </article>

  <article class="grid12 entry" id="aliases">
    <div class="meta">
      <span class="cat mono">{dot("snd")}Aliases</span>
      <h2>Two sonic identities</h2>
      <p>LESEL focuses on experimental electronic textures, while Addison Gardens opens space for blending guitar, improvisation and live performance approaches.</p>
    </div>
    <div class="media" style="grid-template-columns:1fr">
      <iframe class="sc" title="LESEL — OT001 preview" loading="lazy" src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/leselmusic/leselot001-preview&amp;color=%23151515&amp;auto_play=false&amp;show_user=true"></iframe>
    </div>
  </article>

  <article class="entry" id="lesel">
    <div class="section-head" style="border:0;padding:0 0 16px"><h2>LESEL</h2><span class="mono">OT001 EP — 2024 · <a href="https://soundcloud.com/leselmusic" target="_blank" rel="noopener">SoundCloud ↗</a></span></div>
    <div class="sound-grid" data-gallery>{"".join(lesel)}</div>
  </article>

  <article class="grid12 entry" id="addison-gardens">
    <div class="meta">
      <span class="cat mono">{dot("snd")}Alias</span>
      <h2>Addison Gardens</h2>
      <p>A project for experiments with sound — including guitar, live sets, and compositions outside of house frameworks.</p>
    </div>
    <div class="media" style="grid-template-columns:1fr">
      <iframe class="sc tall" title="Addison Gardens" loading="lazy" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/soundcloud%253Atracks%253A925918936&amp;color=%23151515&amp;auto_play=false&amp;visual=true"></iframe>
    </div>
  </article>

  <article class="grid12 entry" id="theatre">
    <div class="meta">
      <span class="cat mono">{dot("snd")}Sound design — 2024</span>
      <h2>Unul Dintre Noi</h2>
      <span class="mono muted">Teatrul de Comedie, Bucharest</span>
      <p>Composed and performed the sonic environment for a stage production, focusing on intimate textures and spatialization.</p>
    </div>
    <div class="media" data-gallery>{frame("udn.jpg", "Unul Dintre Noi", cls="main", w=1400)}</div>
  </article>
</div>"""
    write("sound.html", page("sound.html", "Sound",
        "Sound by Denis Flueraru — LESEL, Addison Gardens, custom instruments, performances and theatre sound design.", body, current="sound.html"))


# ------------------------------------------------------------------ services
def build_services():
    blocks = "".join(f"""<section class="grid12 service">
  <span class="n mono">{i+1:02d}</span>
  <h2>{E(t)}</h2>
  <div class="body"><p>{E(d)}</p><ul class="chips">{"".join(f"<li>{E(c)}</li>" for c in chips)}</ul></div>
</section>""" for i, (t, d, chips) in enumerate(SERVICES))
    body = page_head("Services", "<p>Available for commissions, productions and workshops.</p>"
                     '<a class="link-arrow" href="mailto:contact@atomatlab.com">contact@atomatlab.com →</a>') + \
        f'<div class="wrap">{blocks}<p class="mono" style="padding-top:32px">If you’d like to collaborate, write to '\
        f'<a class="link-arrow" href="mailto:contact@atomatlab.com">contact@atomatlab.com</a></p></div>'
    write("services.html", page("services.html", "Services",
        "Sound design, interactive development, 3D fabrication and creative project development by Denis Flueraru / ATOMAT LAB.",
        body, current="services.html"))


# ------------------------------------------------------------------ bio
CV_EXP = [
    ("2026 —", "HexagonX — BTL Experience Manager", "Bucharest",
     ["Program interactive installations and experiences for brand activations and live events",
      "Lead setup, teardown and on-site technical management, including power distribution and equipment logistics",
      "Develop concepts and prototypes for installations, scenography and event experiences"]),
    ("2021 —", "ATOMAT LAB — Founder", "Bucharest",
     ["Design and build interactive audiovisual installations using creative coding, custom hardware and sound",
      "Coordinate EU-funded cultural projects (Culture Moves Europe) from concept through production",
      "Design and deliver DIY workshops on sound and interaction",
      "Run an online shop, manufacturing contact microphones and other electronic devices"]),
    ("2019 — 2021", "Animotion Production — Sound Designer & Music Producer", "Bucharest",
     ["Composed music and designed sound for advertising campaigns",
      "Recorded, edited and mixed voice-over for TV, radio and digital channels",
      "Synchronised and mastered audio for national and international productions"]),
]
CV_EDU = [
    ("2023", "MA — Interactive Technologies for Performing & Media Arts",
     "UNATC “I.L. Caragiale”, Bucharest — thesis: Designing a Recording Tool for Representing Physical Textures in Sound"),
    ("2017", "BTEC — Music Technology", "Catalyst Institute (dBs Music), Berlin"),
    ("2016", "BA — Film Studies, Television & New Broadcasting Media", "Kingston University, London"),
]
CV_SKILLS = [
    ("Audio & video", "Sound design, music production, spatial audio, custom instruments, live recording, circuit bending. Ableton Live, Pro Tools, Premiere Pro."),
    ("Code & interaction", "Max/MSP, Processing, microcontrollers, IoT, MIDI, electronics. JavaScript, C, HTML, Sonic Pi, TinyML, TensorFlow."),
    ("Fabrication", "3D printing, laser cutting, CNC, power tools. Rhino 3D, Illustrator, UGS."),
    ("Languages", "Romanian (native), English (fluent), French (elementary)."),
]


def build_bio():
    exp = "".join(f'<div class="item"><span class="mono">{d}</span><div><h3>{E(t)}</h3><span class="mono muted">{E(p)}</span>'
                  f'<ul>{"".join(f"<li>{E(x)}</li>" for x in b)}</ul></div></div>' for d, t, p, b in CV_EXP)
    edu = "".join(f'<div class="item"><span class="mono">{d}</span><div><h3>{E(t)}</h3><span class="mono muted">{E(p)}</span></div></div>'
                  for d, t, p in CV_EDU)
    sk = "".join(f'<div class="item"><span class="mono">{E(k)}</span><p>{E(v)}</p></div>' for k, v in CV_SKILLS)
    body = page_head("Biography", "<p>Creative technologist — interactive installations, sound &amp; experience design.</p>"
                     f'<a class="link-arrow" href="{CV_URL}" target="_blank" rel="noopener">Download CV (PDF) ↓</a>') + f"""
<div class="wrap">
  <section class="grid12 bio-top">
    {frame("portrait-bw.jpg", "Portrait", eager=True, alt="Portrait of Denis Flueraru", w=1800)}
    <blockquote>“Even if my background is not really linked with electronics, I formed a tight bond that manifested in a growing interest for technological skills. Now it is always part of my work. This bond unveils itself in a modernist-like, interdisciplinary manner and is either interactivity as it attempts to start a dialogue between the viewer and artwork or the result of the interaction between the inhabited space and technology.”</blockquote>
  </section>
  <section class="grid12 cv"><h2>Experience</h2><div class="list">{exp}</div></section>
  <section class="grid12 cv"><h2>Education</h2><div class="list">{edu}</div></section>
  <section class="grid12 cv"><h2>Skills</h2><div class="list">{sk}</div></section>
  <section class="grid12 cv"><h2>Selected work</h2><div class="list"><div class="item"><span class="mono">Index</span><p>Every project, workshop, collab and exhibition is listed on the <a class="link-arrow" href="index.html#idx-title">home page index →</a></p></div></div></section>
</div>"""
    write("biography.html", page("biography.html", "Biography",
        "Denis Flueraru — creative technologist, founder of ATOMAT LAB, based in Bucharest. Experience, education and skills.",
        body, current="biography.html"))


def build_contact():
    items = [
        ("Email", "flueraru.denis@gmail.com", "mailto:flueraru.denis@gmail.com"),
        ("Studio", "contact@atomatlab.com", "mailto:contact@atomatlab.com"),
        ("Phone", "+40 727 801 918", "tel:+40727801918"),
        ("Instagram", "@denisflueraru", "https://www.instagram.com/denisflueraru/"),
        ("LinkedIn", "in/denisflueraru", "https://www.linkedin.com/in/denisflueraru/"),
        ("YouTube", "@atomatlab", "https://www.youtube.com/@atomatlab"),
        ("TikTok", "@atomatlab", "https://www.tiktok.com/@atomatlab"),
    ]
    lis = "".join(f'<li><a href="{u}"{" target=_blank rel=noopener" if u.startswith("http") else ""}>'
                  f'<span class="k mono">{k}</span><span class="v">{E(v)}</span><span class="mono">→</span></a></li>' for k, v, u in items)
    body = page_head("Contact", "<p>For commissions, workshops, collaborations and press.</p><p>Based in Bucharest, RO.</p>") + \
        f'<div class="wrap"><ul class="contact-list">{lis}</ul></div>'
    write("contact.html", page("contact.html", "Contact", "Get in touch with Denis Flueraru — email, phone and social links.",
                               body, current="contact.html"))


def build_404():
    body = page_head("Lost signal", '<p>This page does not exist.</p><a class="link-arrow" href="index.html">Back to the index →</a>')
    write("404.html", page("404.html", "Not found", "Page not found.", body))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_index(); build_artworks(); build_projects(); build_entries()
    build_sound(); build_services(); build_bio(); build_contact(); build_404()
    print("built", sorted(p.name for p in OUT.glob("*.html")))
