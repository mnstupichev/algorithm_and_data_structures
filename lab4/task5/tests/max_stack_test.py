from random import randint
from utils import time_data, memory_data
from lab4.task5.src.solution import MaxStack, main


def test_push_max():
    stack = MaxStack()
    push = [1, 2, 5, 3, 4, 10]
    expected = [1, 2, 5, 5, 5, 10]

    for index, num in enumerate(push):
        stack.push(num)
        assert stack.max() ==  expected[index]


def test_pop_max():
    stack = MaxStack()
    push = [1, 2, 5, 3, 4, 10]
    for num in push:
        stack.push(num)

    expected = [(10, 10), (4, 5), (3, 5), (5, 5), (2, 2), (1, 1)]

    for i in range(len(push)):
        cur_max, last = stack.max(), stack.pop()
        assert last == expected[i][0]
        assert cur_max == expected[i][1]



def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
