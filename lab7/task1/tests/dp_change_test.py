from utils import time_data, memory_data
from lab7.task1.src.solution import dp_change, main


def test_set1():
    # given
    money = 2
    coins = [1, 3, 4]

    # when
    ans = dp_change(money, coins)

    # then
    assert ans == 2


def test_set2():
    # given
    money = 34
    coins = [1, 3, 4]

    # when
    ans = dp_change(money, coins)

    # then
    assert ans == 9


def test_time():
    # given
    time = time_data(main)

    # then
    assert time < 1


def test_memory_data():
    # given
    cur, peak = memory_data(main)

    # then
    assert cur < 1
    assert peak < 1
