import pytest

from random import randint
from utils import time_data, memory_data
from lab1.task10.src.solution import get_pallindrom, main


def test_one_letter():
    string = "A"
    string = get_pallindrom(string)
    assert string == "A"


def test_zero_letters():
    string = ""
    string = get_pallindrom(string)
    assert string == ""


def test_1():
    string = "AAB"
    string = get_pallindrom(string)
    assert string == "ABA"


def test_2():
    string = "QAZQAZ"
    string = get_pallindrom(string)
    assert string == "AQZZQA"


def test_3():
    string = "ABCDEF"
    string = get_pallindrom(string)
    assert string == "A"


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
