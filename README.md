# Advent of Code 2022

Solutions to the [2022 Advent of Code](https://adventofcode.com/2022) challenge in Python 3.10.
Emphasis is on experimenting with Python and system tooling instead of solving as many problems as possible.
Previous year's solutions:

 - [2021](https://github.com/acviana/Advent-of-Code-2021)
 - [2020](https://github.com/acviana/advent-of-code-2020)
 - [2020 with Dagster](https://github.com/acviana/dagster-advent-of-code)
 - [2019](https://github.com/acviana/advent-of-code-2019)

### Setup Instructions

This project uses [Poetry](https://python-poetry.org/) for dependency management.
Once you have installed Poetry you can setup the project by running `poetry install` in the project directory.
The only requirement to run the project code is the Python 3.10 standard library.

A `requirements.txt` file is included if you prefer to set up your own environment with pip or another tool.

### Execution Instructions

To run the code for a given day use the provided `Makefile`

```console
$ make run day=1

python advent_of_code_2022/day_1.py
Max Calorie Count is: 65912
Top 3 Max Calorie Count is: 195625
```

### Development Instructions

The Poetry development dependencies are installed by default when you run `poetry install --with=dev`. If you are using pip you can install them from the `requirements_dev.txt` file.

A suggested workflow is documented in the `Makefile`.

