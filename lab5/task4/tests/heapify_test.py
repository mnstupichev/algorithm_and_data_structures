from utils import time_data, memory_data
from random import randint
from lab5.task4.src.solution import heap_executing, main
from lab5.task1.src.solution import check_heap, main


def test_set_1():
    # given
    array = [5, 4, 3, 2, 1]

    # when
    heap_executing(array)

    # then
    assert array == [1, 2, 3, 5, 4]


def test_set_2():
    # given
    array = [1, 2, 3, 4, 5]

    # when
    heap_executing(array)

    # then
    assert array == [1, 2, 3, 4, 5]


def test_random():
    # given
    array = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]

    # when
    heap_executing(array)

    # then
    assert check_heap(array) == True


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