"""The slate code colours are the avanserv VS Code theme's, so they move when it does."""

import json
import re

import pytest
from conftest import ROOT

VSX = ROOT.parent / "vsx-avanserv-theme" / "themes" / "AvanservDark.json"

# Our token kind, and a TextMate scope vsx colours with it.
KINDS = {
    "keyword": "keyword",
    "string": "string.quoted",
    "number": "constant.numeric",
    "function": "entity.name.function",
    "error": "invalid",
}


@pytest.mark.skipif(not VSX.is_file(), reason=f"no vsx-avanserv-theme checkout at {VSX}")
def test_slate_values_match_vsx(tokens):
    text = re.sub(r"^\s*//.*$", "", VSX.read_text(), flags=re.M)
    theme = json.loads(re.sub(r",(\s*[}\]])", r"\1", text))
    by_scope = {}
    for rule in theme["tokenColors"]:
        scopes = rule.get("scope", [])
        for scope in [scopes] if isinstance(scopes, str) else scopes:
            by_scope.setdefault(scope, rule["settings"].get("foreground"))
    for kind, scope in KINDS.items():
        assert tokens["dark"][f"--av-syntax-{kind}"] == by_scope[scope].lower(), kind
