import pytest

from random import randint
from utils import time_data, memory_data
from lab2.task1.src.solution import merge_sort, main


def test_already_sorted():
    # given
    array = [1, 2, 3, 4, 5]

    # when
    merged_array = merge_sort(array)

    # then
    assert merged_array == [1, 2, 3, 4, 5]


def test_reversed_array():
    # given
    array = [5, 4, 3, 2, 1]

    # when
    merged_array = merge_sort(array)

    # then
    assert merged_array == [1, 2, 3, 4, 5]


def test_random_order():
    # given
    array = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 3))]

    # when
    sorted_array = sorted(array)
    merged_array = merge_sort(array)

    # then
    assert merged_array == sorted_array


def test_duplicate_elements():
    # given
    array = [0, 0, 0, 0, 0]

    # when
    merged_array = merge_sort(array)

    # then
    assert merged_array == [0, 0, 0, 0, 0]


def test_empty_list():
    # given
    array = []

    # when
    merged_array = merge_sort(array)

    # then
    assert merged_array == []


def test_one_element():
    # given
    array = [0]

    # when
    merged_array = merge_sort(array)

    # then
    assert merged_array == [0]


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
