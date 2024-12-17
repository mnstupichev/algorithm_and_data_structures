from random import randint
from utils import time_data, memory_data
from lab3.task3.src.solution import naive_scarecrow_sort, fast_scarecrow_sort_check, main


def test_empty():
    # given
    k = randint(1, 10 ** 5)
    array = []

    # when
    ans = fast_scarecrow_sort_check(array, k)

    # then
    assert ans == True


def test_one_element():
    # given
    k = randint(1, 10 ** 5)
    array = [1]

    # when
    ans = fast_scarecrow_sort_check(array, k)

    # then
    assert ans == True


def test_random():
    # given
    k = randint(1, 10 ** 5)
    array = [randint(-10 ** 8, 10 ** 8) for _ in range(randint(0, 10 ** 3))]

    # when
    ans = fast_scarecrow_sort_check(array, k)

    # then
    right_ans = naive_scarecrow_sort(array, k) == sorted(array)
    assert ans == right_ans


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