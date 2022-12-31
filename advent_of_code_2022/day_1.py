from typing import List


def load_data() -> List[str]:
    """Load data from the input file."""
    with open("inputs/day_1_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]) -> List[List[int]]:
    """Parse data into lists of integers.

    Probably slightly too cleaver, uses string manipulation by joining
    on `|` and then breaking on `||` to arrive at the result. Couldn't
    find a cleaner way with `itertools`.
    """
    return [
        [int(subitem) for subitem in item.split("|")]
        for item in "|".join(data).split("||")
    ]


def get_sorted_sum(parsed_data: List[List[int]]) -> List[int]:
    """Sums over each sublist and orders the result."""
    return sorted([sum(item) for item in parsed_data])


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)
    sorted_sum_list = get_sorted_sum(parsed_data)
    print(f"Max Calorie Count is: {sorted_sum_list[-1]}")
    print(f"Top 3 Max Calorie Count is: {sum(sorted_sum_list[-3:])}")


if __name__ == "__main__":
    main()
