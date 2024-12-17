from utils import time_data, memory_data
from lab4.task8.src.solution import calculate_polish_notation, main


def test_random_sets():
    # given
    expressions_sets = [
        ["2", "3", "+", "5", "*"],
        ["4", "2", "-"],
        ["10", "2", "*", "3", "+", "4", "-"],
        ["1", "2", "+", "3", "*"],
        ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    ]
    expected = [25, 2, 19, 9, 14]

    for ind, expression in enumerate(expressions_sets):
        # when
        ans = calculate_polish_notation(expression)

        # then
        assert ans == expected[ind]


def test_time():
    # given
    time = time_data(main)

    # then
    assert time < 2


def test_memory_data():
    # given
    cur, peak = memory_data(main)

    # then
    assert cur < 256
    assert peak < 256
