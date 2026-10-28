import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
THEME = ROOT / "src" / "avanserv_zensical_theme"
ASSETS = THEME / "assets" / "avanserv"


def strip_comments(css: str) -> str:
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def scope(css: str, selector_start: str) -> dict[str, str]:
    css = strip_comments(css)
    start = css.index(selector_start)
    body = css[css.index("{", start) + 1 : css.index("}", start)]
    return {k: " ".join(v.split()) for k, v in re.findall(r"(--[a-z0-9-]+)\s*:\s*([^;]+);", body)}


@pytest.fixture(scope="session")
def tokens() -> dict[str, dict[str, str]]:
    """Brand custom properties per colour scheme, dark falling back to light as in the cascade."""
    css = (ASSETS / "tokens.css").read_text()
    light = scope(css, ":root")
    dark = {**light, **scope(css, '[data-md-color-scheme="slate"]')}
    # Syntax colours, with aliases of brand roles resolved in the scheme they are read in.
    syntax = (ASSETS / "syntax.css").read_text()
    blocks = {"light": [":root"], "dark": [":root", '[data-md-color-scheme="slate"]']}
    for scheme, selectors in ((light, blocks["light"]), (dark, blocks["dark"])):
        for selector in selectors:
            for name, value in scope(syntax, selector).items():
                alias = re.fullmatch(r"var\((--[a-z0-9-]+)\)", value)
                scheme[name] = scheme[alias.group(1)] if alias else value
    return {"light": light, "dark": dark}
