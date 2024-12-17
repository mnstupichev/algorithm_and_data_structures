import pytest

from random import randint
from utils import time_data, memory_data
from lab1.task9.src.solution import binary_add, main


def test_only_zeros():
    # given
    a = [0, 0, 0]
    b = [0, 0, 0]

    # when
    c = binary_add(a, b)

    # then
    assert c == [0]


def test_different_length():
    # given
    a = [0, 0, 1]
    b = [1, 0, 1]

    # when
    c = binary_add(a, b)

    # then
    assert c == [1, 1, 0]


def test_random_add():
    for i in range(3):
        # given
        n = randint(0, 10 ** 5)
        a = [randint(0, 1) for _ in range(n)]
        b = [randint(0, 1) for _ in range(n)]

        # when
        c = binary_add(a, b)
        a_10 = int("".join([str(dig) for dig in a]), 2)
        b_10 = int("".join([str(dig) for dig in b]), 2)
        c_10 = a_10 + b_10
        c_2 = bin(c_10)[2:]
        c_2 = list(map(int, c_2))

        # then
        assert c_2 == c


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

