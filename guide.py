"""The words of the guide (/guia/), per language. build.py renders them; edit here, run build.py, commit the HTML.
UI names in «» are the exact strings the app shows in that language (Spanish: Scripts/es_translations.py in the app)."""
import os, runpy
_here = os.path.dirname(os.path.abspath(__file__))
GUIDE = {}
for _lang in ["es", "ca", "en"]:
    _f = os.path.join(_here, "guide_%s.py" % _lang)
    if os.path.exists(_f):
        GUIDE[_lang] = runpy.run_path(_f)["GUIDE_" + _lang.upper()]
