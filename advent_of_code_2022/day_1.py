"""Solutions to the Day 1 puzzle."""

from typing import Dict, List


def load_data() -> List[str]:
    """Load data from the input file with minimal parsing.

    Parameters:
        None

    Returns:
        The input data with one line per item.
    """
    with open("inputs/day_1_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]) -> List[List[int]]:
    """Parse data into lists of integers.

    Probably slightly too cleaver, uses string manipulation by joining
    on ``|`` and then breaking on ``||`` to arrive at the result.
    Couldn't find a cleaner way with itertools.

    Parameters:
        data: output data from :func:`load_data`.

    Returns:
        List of list of integers with each list representing snack
         calories per elf.
    """
    return [
        [int(subitem) for subitem in item.split("|")]
        for item in "|".join(data).split("||")
    ]


def get_sorted_sum(parsed_data: List[List[int]]) -> List[int]:
    """Sums over each sublist and orders the result.

    Parameters:
        parsed_data: The output from :func:`parse_data`.

    Returns:
        Total calories per each elf.
    """
    return sorted([sum(item) for item in parsed_data])


def main() -> Dict[str, int]:
    """
    Solves Day 1.

    Parameters:
        None

    Returns:
        A dictionary contain the part 1 and part 2 solutions.
    """
    data = load_data()
    parsed_data = parse_data(data)
    sorted_sum_list = get_sorted_sum(parsed_data)
    return {
        "top_1": sorted_sum_list[-1],
        "top_3": sum(sorted_sum_list[-3:]),
    }


if __name__ == "__main__":
    solution_dict = main()
    print(f"Max Calorie Count is: {solution_dict['top_1']}")
    print(f"Top 3 Max Calorie Count is: {solution_dict['top_3']}")
