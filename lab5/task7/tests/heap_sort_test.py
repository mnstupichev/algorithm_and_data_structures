from random import randint
from utils import time_data, memory_data
from lab5.task7.src.solution import heap_sort, main


def test_already_sorted():
    array = [1, 2, 3, 4, 5]
    heap_sort(array)
    assert array == [1, 2, 3, 4, 5]


def test_reversed_array():
    array = [5, 4, 3, 2, 1]
    heap_sort(array)
    assert array == [1, 2, 3, 4, 5]


def test_random_order():
    array = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 3))]
    heap_sort(array)
    sorted_array = sorted(array)
    assert array == sorted_array


def test_duplicate_elements():
    array = [0, 0, 0, 0, 0]
    heap_sort(array)
    assert array == [0, 0, 0, 0, 0]


def test_empty_list():
    array = []
    heap_sort(array)
    assert array == []


def test_one_element():
    array = [0]
    heap_sort(array)
    assert array == [0]

def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
