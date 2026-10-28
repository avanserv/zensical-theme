# zensical-theme

The avanserv theme for [Zensical](https://zensical.org/) documentation sites: the brand palette in
both colour schemes, self-hosted Spline Sans, the mark and favicon, and kit styling for admonitions,
code, tables, tabs, navigation and the table of contents. Product docs such as odouche and odooscan
install it from a tag.

Documentation and a page of every styled element: <https://avanserv.github.io/zensical-theme/>.

## Use it

```toml
# pyproject.toml, in the group that holds zensical
"avanserv-zensical-theme @ git+https://github.com/avanserv/zensical-theme@v0.1.0"
```

```toml
# zensical.toml
[project.theme]
name = "avanserv"
```

Drop the site's own `[[project.theme.palette]]`, `font` and `icon.logo` settings; the theme supplies
them.

## Work on it

```sh
uv sync
make site-serve   # the theme's own site, rebuilt on save
make check        # ruff, pytest, brand drift check, strict build
```

The package directory `src/avanserv_zensical_theme/` is the theme. It extends Zensical's built-in
theme through `mkdocs_theme.yml` and overrides only blocks and small partials, never `base.html` or
`partials/header.html`, so it keeps working across Zensical releases. Styles live in
`assets/avanserv/theme.css`, which may reference brand custom properties but no colour literals.

## Brand artefacts

`avanserv/brand` is private and this repository is public, so the fonts, favicons, mark geometry and
palette are vendored. `make sync-brand` regenerates them from a checkout at the tag in
`BRAND_VERSION` (from `../brand`, or `BRAND_DIR`); never edit them by hand. `make brand-check` fails on
drift and skips with a warning when no checkout is reachable. In CI it needs the `BRAND_DEPLOY_KEY`
secret, a read-only deploy key on `avanserv/brand`.

## Licence

MIT for the code. The avanserv name, mark and favicons are trademarks and the fonts are under the
SIL Open Font License; see `NOTICE`.
