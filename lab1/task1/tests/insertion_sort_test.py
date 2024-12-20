import pytest

from random import randint
from utils import time_data, memory_data
from lab1.task1.src.solution import insertion_sort, main


def test_already_sorted():
    # given
    array = [1, 2, 3, 4, 5]

    # when
    array = insertion_sort(array)

    # then
    assert array == [1, 2, 3, 4, 5]


def test_reversed_array():
    # given
    array = [5, 4, 3, 2, 1]

    # when
    array = insertion_sort(array)

    # then
    assert array == [1, 2, 3, 4, 5]


def test_random_order():
    # given
    array = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 3))]

    # when
    array = insertion_sort(array)
    sorted_array = sorted(array)

    # then
    assert array == sorted_array


def test_duplicate_elements():
    # given
    array = [0, 0, 0, 0, 0]

    # when
    array = insertion_sort(array)

    # then
    assert array == [0, 0, 0, 0, 0]


def test_empty_list():
    # given
    array = []

    # when
    array = insertion_sort(array)

    # then
    assert array == []


def test_one_element():
    # given
    array = [0]

    # when
    array = insertion_sort(array)

    # then
    assert array == [0]


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