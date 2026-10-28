.PHONY: sync-brand brand-check lint test site site-serve check clean

# Vendors avanserv/brand@$(cat BRAND_VERSION) from $BRAND_DIR (default ../brand).
sync-brand:
	uv run python tools/sync_brand.py

brand-check:
	uv run python tools/sync_brand.py --check

lint:
	uv run ruff check
	uv run ruff format --check

test:
	uv run pytest

site:
	uv run zensical build --clean --strict

site-serve:
	uv run zensical serve

check: lint test brand-check site

clean:
	rm -rf site .cache .pytest_cache .ruff_cache
