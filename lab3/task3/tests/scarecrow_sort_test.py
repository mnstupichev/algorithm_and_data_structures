import pytest

from random import randint
from utils import time_data, memory_data
from lab3.task3.src.solution import naive_scarecrow_sort, fast_scarecrow_sort_check, main


def test_empty():
    k = randint(1, 10**5)
    array = []
    ans = fast_scarecrow_sort_check(array, k)
    assert ans == True


def test_one_element():
    k = randint(1, 10 ** 5)
    array = [1]
    ans = fast_scarecrow_sort_check(array, k)
    assert ans == True



def test_random():
    k = randint(1, 10 ** 5)
    array = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 3))]
    ans = fast_scarecrow_sort_check(array, k)
    right_ans = naive_scarecrow_sort(array, k) == sorted(array)
    assert ans == right_ans


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
