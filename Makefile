black:
	black advent_of_code_2022
	black tests

black-diff:
	black advent_of_code_2022 --diff
	black tests --diff

export:
	poetry export -f requirements.txt -o requirements.txt
	poetry export -f requirements.txt -o requirements_dev.txt --dev

flake8:
	flake8 advent_of_code_2022/ tests/ --statistics

install:
	poetry install

pre-commit: black flake8 test

run:
	python advent_of_code_2022/day_$(day).py

setup-day:
	touch advent_of_code_2022/day_$(day).py
	touch tests/day_$(day)_test.py
	touch inputs/day_$(day)_input.txt
	touch puzzles/day_$(day).md

setup-day-with-template:
	cp -vn advent_of_code_2022/template_module.py advent_of_code_2022/day_$(day).py
	cp -vn advent_of_code_2022/template_test.py tests/day_$(day)_test.py
	touch inputs/day_$(day)_input.txt
	touch puzzles/day_$(day).md

stage-day:
	git add advent_of_code_2022/day_$(day).py
	git add tests/day_$(day)_test.py
	git add inputs/day_$(day)_input.txt
	git add puzzles/day_$(day).md

test:
	pytest -vvs --cov-report term-missing --cov=advent_of_code_2022 tests/

_update:
	poetry update

update: _update export pre-commit

update-diff:
	poetry update --dry-run | grep -i updat
