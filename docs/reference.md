# Reference

## What the theme sets

| Setting | Value | Source |
| --- | --- | --- |
| `variant` | `modern` | `mkdocs_theme.yml` |
| `font` | `false`, so no Google Fonts request | `mkdocs_theme.yml` |
| `favicon` | the brand favicon, with `.ico` and Apple touch icon beside it | `main.html` |
| `palette` | system, light and dark toggles, `primary` and `accent` set to `custom` | `mkdocs_theme.yml` |
| Logo | the outline mark, drawn in `currentColor` | `partials/logo.html` |
| Footer | the site's `copyright`, then a link to avanserv | `partials/copyright.html` |
| Code colours | the avanserv VS Code theme in dark, a matching AA variant in light | `assets/avanserv/syntax.css` |

## What a site may change

- `features`, `language`, `markdown_extensions`, `nav` and everything outside `[project.theme]`.
- The palette toggles' icons and labels, by redefining all three `[[project.theme.palette]]` entries
  with `primary = "custom"` and `accent = "custom"` kept on each.
- `theme.logo`, to show an image instead of the mark. Product docs keep the mark: a product owns its
  name and nothing else of the identity.

## What a site should not change

Colours, type and radii. They come from `avanserv/brand`, so a local override drifts from every other
avanserv surface the next time the brand moves. Raise the change on the brand instead.

## Colours

The theme exposes the brand's role tokens as custom properties, so a page that needs a colour can
name the role rather than a value:

| Property | Use |
| --- | --- |
| `--color-content`, `--color-content-muted`, `--color-content-faint` | text, by emphasis |
| `--color-canvas`, `--color-card` | page ground and raised surfaces |
| `--color-line`, `--color-line-subtle` | borders and dividers |
| `--color-link`, `--color-accent` | links and the one point of emphasis per view |
| `--color-info`, `--color-success`, `--color-warning`, `--color-danger` | status |

## Updating the brand

The brand artefacts are vendored, because this repository is public and `avanserv/brand` is not.
With a checkout of the brand at the new tag beside this repository:

```sh
echo v0.4.0 > BRAND_VERSION
make sync-brand
make check
```

`make brand-check` fails when the vendored files differ from the pinned tag, and skips with a
warning when no brand checkout is reachable.
