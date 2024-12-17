from random import randint
from utils import time_data, memory_data
from lab4.task5.src.solution import MaxStack, main


def test_push_max():
    # given
    stack = MaxStack()
    push = [1, 2, 5, 3, 4, 10]
    expected = [1, 2, 5, 5, 5, 10]

    for index, num in enumerate(push):
        # when
        stack.push(num)

        # then
        assert stack.max() == expected[index]


def test_pop_max():
    # given
    stack = MaxStack()
    push = [1, 2, 5, 3, 4, 10]
    for num in push:
        stack.push(num)
    expected = [(10, 10), (4, 5), (3, 5), (5, 5), (2, 2), (1, 1)]

    for i in range(len(push)):
        # when
        cur_max, last = stack.max(), stack.pop()

        # then
        assert last == expected[i][0]
        assert cur_max == expected[i][1]


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