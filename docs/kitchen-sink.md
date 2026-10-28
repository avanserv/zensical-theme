# Kitchen sink

Every element the theme styles, on one page. Body text runs at the brand's body role, with links
like [the Zensical documentation](https://zensical.org/docs/) underlined at rest, **strong text**
at weight 600, *emphasis*, `inline code`, ==marked text==, ++ctrl+shift+p++ keys and a
footnote.[^1]

[^1]: Footnotes render at the foot of the page.

## Headings

### Third level

#### Fourth level

A paragraph under the smallest heading the product docs use.

## Admonitions

!!! note
    The default callout. Note, abstract, info and todo take the info tone.

!!! tip "Pin an exact tag"
    The tip, success and check types take the success tone.

!!! warning
    Warning and question take the warning tone.

!!! danger "This rewrites history"
    Danger, failure, error and bug take the danger tone.

!!! example
    Example, quote and cite take the neutral tone.

??? info "A collapsed details block"
    Details share the admonition styling and open on click.

???+ question "An open details block"
    Starts expanded.

## Code

```python title="odouche/client.py" linenums="1" hl_lines="3 4"
from odouche import Client

client = Client.from_env()
for project in client.projects.list():  # (1)!
    print(project.name, project.odoo_version)
```

1.  Annotations open a tooltip from the marker in the code.

Untitled blocks, one per language the product docs use most:

```python
import functools


@functools.cache
def resolve(path: str, *, strict: bool = True) -> dict | None:
    # A missing path is an error only in strict mode.
    if not path and strict:
        raise ValueError(f"empty path: {path!r}")
    return {"path": path, "depth": path.count(".") + 1, "ok": True} or None


class Index:
    def __init__(self, modules: list[str]) -> None:
        self.modules = sorted(set(modules))
```

```toml
[project.theme]
name = "avanserv"
features = ["content.code.copy", "navigation.footer"]

[project.markdown_extensions.toc]
permalink = true
depth = 3
```

```console
$ uv run oscn check addons/ --series 18.0
addons/sale_custom/models/sale_order.py:88:5: OD203 unresolved-field-path
Found 1 finding.
```

A long line scrolls inside its block rather than widening the page:

```text
2026-10-28T09:14:03Z INFO  scanning addons/sale_custom against the 18.0 index: 412 modules, 9 812 manifests, 1 finding at addons/sale_custom/models/sale_order.py:88
```

## Content tabs

=== "uv"

    ```sh
    uv add --group docs "avanserv-zensical-theme @ git+https://github.com/avanserv/zensical-theme@v0.1.0"
    ```

=== "pip"

    ```sh
    pip install "avanserv-zensical-theme @ git+https://github.com/avanserv/zensical-theme@v0.1.0"
    ```

=== "Notes"

    A tab can hold prose as well as code. It keeps the card's padding:

    - Pin an exact tag rather than a branch.
    - Run `uv lock` after changing the pin.

## Tables

| Rule | Severity | Since | Summary |
| --- | --- | ---: | --- |
| `OD101` | error | 0.1.0 | Manifest declares a dependency that is not installed |
| `OD203` | warning | 0.3.0 | Field overrides a parent field with a different type |
| `OD310` | info | 0.4.2 | View inherits a record that the series removed |

## Lists

- An unordered list item.
- A second item with nested content:
    - A nested item.
    - Another nested item.

An ordered list:

1. An ordered list item.
2. A second ordered item.

A task list:

- [x] A completed task
- [ ] An open task

Term
:   A definition list entry, used for options and flags.

## Quotes and rules

> A blockquote sits muted behind a left rule, for quoted output or a cited passage.

---

## Buttons

[Get started](index.md){ .md-button .md-button--primary }
[Reference](reference.md){ .md-button }
