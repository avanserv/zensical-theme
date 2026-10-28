"""Characters nobody types by hand stay out of what this repository writes (WRITING.md)."""

import re

from conftest import ROOT, THEME

# Long dashes, curly quotes, ellipsis, no-break space, bullet and check glyphs, then emoji.
_POINTS = (0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2026, 0x00A0, 0x2022)
_POINTS += (0x2713, 0x2714, 0x2717, 0x2718)
REJECTED = re.compile(
    "["
    + "".join(map(chr, _POINTS))
    + chr(0x2600)
    + "-"
    + chr(0x27BF)
    + chr(0x1F000)
    + "-"
    + chr(0x1FAFF)
    + "]"
)
BRAND = THEME / "assets" / "avanserv" / "brand"


def authored():
    roots = [ROOT / "docs", ROOT / "tools", ROOT / "tests", THEME, ROOT / ".github"]
    files = [ROOT / name for name in ("README.md", "NOTICE", "Makefile", "zensical.toml")]
    for root in roots:
        files += [p for p in root.rglob("*") if p.is_file() and BRAND not in p.parents]
    return [p for p in files if p.suffix not in {".pyc", ".woff2", ".png", ".ico"}]


def test_no_rejected_characters():
    hits = []
    for path in authored():
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if REJECTED.search(line):
                hits.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()[:80]}")
    assert hits == []
