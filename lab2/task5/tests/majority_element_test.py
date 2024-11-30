import pytest

from random import randint
from utils import time_data, memory_data
from lab2.task5.src.solution import majority_element, main


def test_empty():
    array = []
    majority = majority_element(array)
    assert majority is None


def test_one_element():
    array = [1]
    majority = majority_element(array)
    assert majority == 1


def test_from_task_1():
    array = [2, 3, 9, 2, 2]
    majority = majority_element(array)
    assert majority == 2


def test_from_task_2():
    array = [1, 2, 3, 4]
    majority = majority_element(array)
    assert majority is None


def test_random():
    array = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 3))]
    majority = majority_element(array)
    elements = set(array)
    majority_true = None
    for el in elements:
        if array.count(el) > len(array) / 2:
            majority_true = el
            break
    assert majority == majority_true


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
