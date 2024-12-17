import pytest

from random import randint
from utils import time_data, memory_data
from lab1.task10.src.solution import get_pallindrom, main


def test_one_letter():
    # given
    string = "A"

    # when
    string = get_pallindrom(string)

    # then
    assert string == "A"


def test_zero_letters():
    # given
    string = ""

    # when
    string = get_pallindrom(string)

    # then
    assert string == ""


def test_1():
    # given
    string = "AAB"

    # when
    string = get_pallindrom(string)

    # then
    assert string == "ABA"


def test_2():
    # given
    string = "QAZQAZ"

    # when
    string = get_pallindrom(string)

    # then
    assert string == "AQZZQA"


def test_3():
    # given
    string = "ABCDEF"

    # when
    string = get_pallindrom(string)

    # then
    assert string == "A"


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