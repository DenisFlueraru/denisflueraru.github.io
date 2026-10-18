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

-------------------------------------------------------------------------------
ADDING A WORKSHOP, COLLAB, EXHIBITION OR ARTWORK — three steps
-------------------------------------------------------------------------------

1. Put the photos in a folder inside ../DRIVE-IMAGES, e.g.
       DRIVE-IMAGES/WORKSHOPS/Libra Bank/Libra1.JPG, Libra2.JPG, Libra3.JPG
   Name them 1, 2, 3... — they are imported in filename order, and the first one
   becomes the big photo.

2. Import them (folder inside DRIVE-IMAGES, then the name they get in media/):

       python3 _build/import_photos.py "WORKSHOPS/Libra Bank" workshops/libra

   It resizes each photo twice — a full version and a small one for the grids —
   and prints the exact `main=` and `grid=` lines to paste in step 3.

3. Open _build/content.py, copy an existing entry in the right list
   (WORKSHOPS, COLLABS, EXHIBITIONS or ARTWORKS), change the words, and paste
   the lines from step 2. Newest goes at the top of the list. Then:

       python3 _build/build.py

   That rewrites every page. The home index picks the new entry up by itself —
   you never edit an .html file by hand; the build overwrites them.

   An entry needs: id (lowercase, no spaces — it becomes the #link), title,
   year, place, text, main, grid. Optional: video="<YouTube id>".

   Two grid photos sit side by side, three or four fill the row. Any number works.

Then commit and push in GitHub Desktop, the same as always.

-------------------------------------------------------------------------------

Photos that came from Google Drive originally use the older route: add a line to
_build/drive_map.tsv (Drive file id, folder, file name), run
`python3 _build/import_drive.py`, then `python3 _build/build.py`. New photos do
not need this — use import_photos.py above.
