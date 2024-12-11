from utils import time_data, memory_data
from random import randint
from lab5.task4.src.solution import heap_executing, main
from lab5.task1.src.solution import check_heap, main

def test_set_1():
    array = [5, 4, 3, 2, 1]
    heap_executing(array)
    assert array == [1, 2, 3, 5, 4]


def test_set_2():
    array = [1, 2, 3, 4, 5]
    heap_executing(array)
    assert array == [1, 2, 3, 4, 5]


def test_random():
    array = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
    heap_executing(array)
    assert check_heap(array) == True


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
