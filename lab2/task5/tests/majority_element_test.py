import pytest

from random import randint
from utils import time_data, memory_data
from lab2.task5.src.solution import majority_element, main


def test_empty():
    # given
    array = []

    # when
    majority = majority_element(array)

    # then
    assert majority is None


def test_one_element():
    # given
    array = [1]

    # when
    majority = majority_element(array)

    # then
    assert majority == 1


def test_from_task_1():
    # given
    array = [2, 3, 9, 2, 2]

    # when
    majority = majority_element(array)

    # then
    assert majority == 2


def test_from_task_2():
    # given
    array = [1, 2, 3, 4]

    # when
    majority = majority_element(array)

    # then
    assert majority is None


def test_random():
    # given
    array = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 3))]

    # when
    majority = majority_element(array)
    elements = set(array)
    majority_true = None
    for el in elements:
        if array.count(el) > len(array) / 2:
            majority_true = el
            break

    # then
    assert majority == majority_true


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
