import pytest

from advent_of_code_2022.day_1 import get_max, parse_data


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


def test_get_max(input_data):
    assert get_max(parse_data(input_data)) == 24000
