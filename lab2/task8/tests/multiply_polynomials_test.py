import pytest

from random import randint
from utils import time_data, memory_data
from lab2.task8.src.solution import multiply_polynomials, main


def test_empty_polynomials():
    # given
    first = []
    second = []

    # when
    result = multiply_polynomials(first, second)

    # then
    assert result == []


def test_one_element():
    # given
    first = [1]
    second = [2]

    # when
    result = multiply_polynomials(first, second)

    # then
    assert result == [2]


def test_negative_koefs():
    # given
    first = [-1, 2]
    second = [3, -4]

    # when
    result = multiply_polynomials(first, second)

    # then
    assert result == [-3, 10, -8]


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