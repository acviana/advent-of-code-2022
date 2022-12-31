from typing import List


def load_data() -> List[str]:
    with open("inputs/day_1_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]):
    return [
        [int(subitem) for subitem in item.split("|")]
        for item in "|".join(data).split("||")
    ]


def get_max(parsed_data):
    return max([sum(item) for item in parsed_data])


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)
    max_value = get_max(parsed_data)
    print(f"Max Calorie Count is: {max_value}")


if __name__ == "__main__":
    main()
