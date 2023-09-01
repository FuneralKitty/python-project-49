install:
	poetry install

build:
	poetry build

publish: 
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry -m run brain_games

brain-even:
	poetry -m run brain-even_game.py
	
brain-calc:
	poetry -m run brain_calc.py

brain-gcd:
	poetry -m run brain_gcd.py

brain-progression:
	poetry -m run brain_progression.py

brain-prime:
	poetry -m run brain_prime.py

make lint:
	poetry run flake8 brain_games