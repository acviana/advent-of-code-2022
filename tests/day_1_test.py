import pytest

from advent_of_code_2022.day_1 import get_sorted_sum, main, parse_data


@pytest.fixture
def input_data():
    return [
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]


def test_parse_data(input_data):
    expected_parsed_data = [
        [2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    assert parse_data(input_data) == expected_parsed_data


def test_get_sorted_sum(input_data):
    expected_sorted_sum = [4000, 5000, 10000, 11000, 24000]
    assert get_sorted_sum(parse_data(input_data)) == expected_sorted_sum


def test_main():
    expected_solution = {
        "top_1": 65912,
        "top_3": 195625,
    }
    assert expected_solution == main()
