DENISFLUERARU.COM — site v2 (Look A · Index)

To publish: copy everything in this folder (html files, assets/, media/) into the root of the
GitHub Pages repo, replacing the old pages. All file and folder names are lowercase on purpose —
GitHub Pages treats upper and lower case as different, so this avoids broken links.

- assets/site.css, assets/site.js   shared style + behaviour for every page
- media/                            all site photos, resized (from ../IMAGES and ../DRIVE-IMAGES)
- media/drive/                      the former Google Drive photos; *.sm.jpg = small versions for grids
- _build/                           content.py + build.py — edit content.py and run
                                    `python3 _build/build.py` to regenerate the pages
                                    (folders starting with _ are not published by GitHub Pages)

Heartbroken photos are in media/heartbroken/.

Keep the CNAME file — it points GitHub Pages at denisflueraru.com.

Adding photos from Drive later: put them in ../DRIVE-IMAGES, add a line to _build/drive_map.tsv
(Drive file id, folder, file name), run `python3 _build/import_drive.py`, then `python3 _build/build.py`.
