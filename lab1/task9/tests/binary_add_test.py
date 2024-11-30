import pytest

from random import randint
from utils import time_data, memory_data
from lab1.task9.src.solution import binary_add, main


def test_only_zeros():
    a = [0, 0, 0]
    b = [0, 0, 0]
    c = binary_add(a, b)
    assert c == [0]


def test_different_length():
    a = [0, 0, 1]
    b = [1, 0, 1]
    c = binary_add(a, b)
    assert c == [1, 1, 0]


def test_random_add():
    for i in range(3):
        n = randint(0, 10 ** 5)
        a = [randint(0, 1) for _ in range(n)]
        b = [randint(0, 1) for _ in range(n)]
        c = binary_add(a, b)
        a_10 = int("".join([str(dig) for dig in a]), 2)
        b_10 = int("".join([str(dig) for dig in b]), 2)
        c_10 = a_10 + b_10
        c_2 = bin(c_10)[2:]
        c_2 = list(map(int, c_2))
        assert c_2 == c


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1

