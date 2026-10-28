import re

from conftest import ASSETS, strip_comments

THEME_CSS = strip_comments((ASSETS / "theme.css").read_text())
SYNTAX_CSS = strip_comments((ASSETS / "syntax.css").read_text())

# Pure black is allowed only as the shadow ink of the kit's dark-scheme ambient shadow.
SHADOW_INK = re.compile(r"rgb\(0 0 0 / [0-9.]+\)")


def test_theme_css_has_no_colour_literals():
    text = SHADOW_INK.sub("", THEME_CSS)
    assert not re.findall(r"#[0-9a-fA-F]{3,8}\b", text)
    assert not re.findall(r"\b(?:rgba?|hsla?|oklch|oklab|lab|lch|hwb)\(", text)


def test_syntax_literals_are_only_token_definitions():
    for line in SYNTAX_CSS.splitlines():
        if re.search(r"#[0-9a-fA-F]{3,8}\b", line):
            assert re.fullmatch(r"\s*--av-syntax-[a-z]+: #[0-9a-f]{6};", line), line


def test_every_brand_property_used_is_defined(tokens):
    css = THEME_CSS + SYNTAX_CSS
    defined = set(tokens["light"]) | set(re.findall(r"(--av-[a-z0-9-]+)\s*:", css))
    used = set(re.findall(r"var\((--(?!md-)[a-z0-9-]+)", css))
    assert used - defined == set()


def test_tokens_cover_both_schemes(tokens):
    for name in ("--color-canvas", "--color-card", "--color-content", "--color-link"):
        assert tokens["light"][name] != tokens["dark"][name], name
