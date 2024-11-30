import pytest

from random import randint
from utils import time_data, memory_data
from lab2.task8.src.solution import multiply_polynomials, main


def test_empty_polynomials():
    first = []
    second = []
    result = multiply_polynomials(first, second)
    assert result == []


def test_one_element():
    first = [1]
    second = [2]
    result = multiply_polynomials(first, second)
    assert result == [2]


def test_negative_koefs():
    first = [-1, 2]
    second = [3, -4]
    result = multiply_polynomials(first, second)
    assert result == [-3, 10, -8]


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
