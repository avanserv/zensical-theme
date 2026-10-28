import hashlib
import json
import re

from conftest import ASSETS, THEME

MANIFEST = json.loads((ASSETS / "brand" / "manifest.json").read_text())


def test_vendored_files_match_the_brand_release():
    for dest, entry in MANIFEST["files"].items():
        data = (THEME / dest).read_bytes()
        if entry["headed"]:
            first, _, data = data.partition(b"\n")
            assert f"Brand-Source: avanserv/brand@{MANIFEST['brand']}".encode() in first, dest
        assert hashlib.sha256(data).hexdigest() == entry["sha256"], dest


def test_marks_draw_the_brand_geometry():
    for partial in ("av-mark.html", "av-mark-solid.html"):
        html = (THEME / "partials" / partial).read_text()
        assert re.search(r' d="([^"]+)"', html).group(1) == MANIFEST["path"], partial


def test_brand_version_is_pinned_consistently():
    pinned = (THEME.parent.parent / "BRAND_VERSION").read_text().strip()
    assert MANIFEST["brand"] == pinned
