"""WCAG AA for the text pairs the theme draws, in both schemes.

The threshold and the scope come from brand/docs/foundations/contrast.md.
"""

import re

import pytest


def rgba(value: str) -> tuple[float, float, float, float]:
    if value.startswith("#"):
        return (*(int(value[i : i + 2], 16) for i in (1, 3, 5)), 1.0)
    r, g, b, a = re.fullmatch(r"rgb\((\d+) (\d+) (\d+) / ([0-9.]+)\)", value).groups()
    return int(r), int(g), int(b), float(a)


def over(fg: str, bg: tuple[float, float, float]) -> tuple[float, float, float]:
    r, g, b, a = rgba(fg)
    return tuple(c * a + under * (1 - a) for c, under in zip((r, g, b), bg, strict=True))


def luminance(rgb: tuple[float, float, float]) -> float:
    def channel(c: float) -> float:
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, *grounds: str, tokens: dict[str, str]) -> float:
    # Grounds are listed bottom up: the canvas first, then translucent layers over it.
    base = rgba(tokens[grounds[0]])[:3]
    for ground in grounds[1:]:
        base = over(tokens[ground], base)
    text = over(tokens[fg], base)
    hi, lo = sorted((luminance(text), luminance(base)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


PAIRS = [
    ("--color-content", ("--color-canvas",)),
    ("--color-content", ("--color-card",)),
    ("--color-content-muted", ("--color-canvas",)),
    ("--color-content-muted", ("--color-card-header",)),
    ("--color-content-faint", ("--color-canvas",)),
    ("--color-link", ("--color-canvas",)),
    ("--color-link", ("--color-card",)),
    ("--color-content", ("--color-canvas", "--color-control-selected")),
    # Code blocks sit on the card; inline code on line-subtle over the canvas.
    ("--color-content-muted", ("--color-card",)),
    ("--color-content-faint", ("--color-card",)),
    ("--color-info", ("--color-card",)),
    ("--color-success", ("--color-card",)),
    ("--color-warning", ("--color-card",)),
    ("--color-danger", ("--color-card",)),
    ("--color-content", ("--color-card", "--color-accent-wash-strong")),
    ("--color-content", ("--color-canvas", "--color-line-subtle")),
    # Code tokens on the code ground and on a highlighted line's band.
    *(
        (f"--av-syntax-{kind}", grounds)
        for kind in ("keyword", "string", "number", "function", "error")
        for grounds in (("--color-card",), ("--color-card", "--av-syntax-band"))
    ),
    ("--av-syntax-comment", ("--color-card", "--av-syntax-band")),
    ("--av-syntax-variable", ("--color-card", "--av-syntax-band")),
    # The primary button.
    ("--color-on-dark-strong", ("--color-accent",)),
]


@pytest.mark.parametrize("scheme", ["light", "dark"])
@pytest.mark.parametrize(("fg", "grounds"), PAIRS, ids=[f"{f}/{'+'.join(g)}" for f, g in PAIRS])
def test_text_meets_aa(tokens, scheme, fg, grounds):
    assert ratio(fg, *grounds, tokens=tokens[scheme]) >= 4.5
