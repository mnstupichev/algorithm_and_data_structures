from utils import time_data, memory_data
from lab4.task8.src.solution import calculate_polish_notation, main


def test_random_sets():
    expressions_sets = [
        ["2", "3", "+", "5", "*"],  # 25
        ["4", "2", "-"],  # 2
        ["10", "2", "*", "3", "+", "4", "-"],  # 19
        ["1", "2", "+", "3", "*"],  # 9
        ["5", "1", "2", "+", "4", "*", "+", "3", "-"]  # 14
    ]
    expected = [25, 2, 19, 9, 14]

    for ind, expression in enumerate(expressions_sets):
        assert calculate_polish_notation(expression) == expected[ind]


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
