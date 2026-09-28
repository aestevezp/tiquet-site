# tiquet-site

Static site for Tiquet, live at https://tiquet.securlabs.net (GitHub Pages from `main`, root; HTTPS enforced).
Spanish at the root (the App Store starts in Spain), English at /en/, Catalan at /ca/; the old /es/ addresses redirect. Edit `build.py` (strings in en/es/ca), run `python3 build.py`, commit the generated HTML and push `main`: Pages
publishes it in a minute or two. Screenshots come from the app's sample data only (invented household).

Published on 2026-09-28 as one clean commit (repo `aestevezp/tiquet-site`, the owner's personal account, like
decksweep-site). DNS at GoDaddy: CNAME `tiquet` → `aestevezp.github.io`. The history before publishing stays only
on the owner's Mac, in the local branch `history-before-publish` (it held an Apple Maps street picture of a real street).

Pushing: the Mac's keychain holds the work account's GitHub credential, which can't write here. Push as the owner's
personal account through gh: `gh auth switch -u aestevezp`, then
`git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push origin main`, then switch back.
