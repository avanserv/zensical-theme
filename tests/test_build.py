"""Build the theme's own site and check what the theme puts on the page."""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from conftest import ROOT


@pytest.fixture(scope="module")
def site(tmp_path_factory) -> Path:
    project = tmp_path_factory.mktemp("project")
    shutil.copytree(ROOT / "docs", project / "docs")
    shutil.copy(ROOT / "zensical.toml", project / "zensical.toml")
    subprocess.run(
        [sys.executable, "-m", "zensical", "build", "--clean", "--strict"],
        cwd=project,
        check=True,
        capture_output=True,
    )
    return project / "site"


def test_theme_stylesheets_and_fonts_are_linked(site):
    html = (site / "index.html").read_text()
    for href in (
        "brand/fonts.css",
        "brand/base.css",
        "avanserv/tokens.css",
        "avanserv/theme.css",
        "avanserv/syntax.css",
    ):
        assert f"assets/avanserv/{href.removeprefix('avanserv/')}" in html, href
    assert "assets/avanserv/search.js" in html
    assert "fonts.googleapis.com" not in html
    assert "fonts.gstatic.com" not in html


def test_assets_are_published(site):
    for path in (
        "assets/avanserv/theme.css",
        "assets/avanserv/tokens.css",
        "assets/avanserv/brand/favicon.svg",
        "assets/avanserv/brand/favicon.ico",
        "assets/avanserv/brand/fonts/spline-sans-latin.woff2",
    ):
        assert (site / path).is_file(), path


def test_header_draws_the_mark_and_footer_credits_avanserv(site):
    html = (site / "index.html").read_text()
    assert 'class="av-mark"' in html
    assert 'assets/avanserv/brand/favicon.svg"' in html
    assert "made by avanserv" in html
