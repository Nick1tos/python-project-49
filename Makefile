setup: install brain-games build publish package-install

install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
make lint:
	poetry run flake8 brain_games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
brain-prog:
	poetry run brain-prog
brain-prime:
	poetry run brain-prime
