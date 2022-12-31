from typing import List


def load_data() -> List[str]:
    """Load data with minimal manipulation"""
    with open("inputs/day_X_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: List[str]):
    """Parse data upto the point where the final calculation can be
    performed.
    """
    pass


def main() -> None:
    """The final answer."""
    data = load_data()
    parse_data(data)
    return None


if __name__ == "__main__":
    answer = main()
    print(f"The answer is {answer}")
