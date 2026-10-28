# zensical-theme

The avanserv theme for [Zensical](https://zensical.org/) documentation sites. It ships the brand
palette in both colour schemes, self-hosted Spline Sans, the mark in the header and the favicon, and
styling for every Markdown element the product docs use.

## Install

Add the theme to the dependency group that already holds Zensical, pinned to a tag:

```toml title="pyproject.toml"
[dependency-groups]
docs = [
    "zensical>=0.0.68",
    "avanserv-zensical-theme @ git+https://github.com/avanserv/zensical-theme@v0.1.0",
]
```

Then select it in `zensical.toml`:

```toml title="zensical.toml"
[project.theme]
name = "avanserv"
```

That is the whole setup. Remove any `[[project.theme.palette]]`, `font` or `icon.logo` settings
the site carried for the stock theme: the theme supplies them, and a site value replaces the
theme's outright.

## Build

```sh
uv sync --locked
uv run zensical build --clean --strict
```

The [kitchen sink](kitchen-sink.md) renders every element the theme styles, in whichever scheme the
toggle in the header selects.
