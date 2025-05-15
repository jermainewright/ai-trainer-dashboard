.PHONY: install-api install-web run-api run-web lint test

install-api:
	cd apps/api && pip install -e .

install-web:
	cd apps/web && npm install

run-api:
	cd apps/api && uvicorn app.main:app --reload --port 8000

run-web:
	cd apps/web && npm run dev

lint:
	cd apps/api && ruff check app
	cd apps/web && npm run lint

test:
	cd apps/api && pytest -q
