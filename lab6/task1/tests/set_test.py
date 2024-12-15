from utils import time_data, memory_data
from lab6.task1.src.solution import Set, main
from random import randint


def test_add():
    # given
    new_set = set()
    to_add = [randint(-10**9, 10**9) for _ in range(10**3)]

    for item in to_add:
        # when
        new_set.add(item)

        # then
        assert item in new_set


def test_remove():
    # given
    new_set = set()
    to_add = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
    for item in to_add:
        new_set.add(item)
    to_remove = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]


    for item in to_remove:
        # when
        if item in new_set:
            new_set.remove(item)

            # then
            assert item not in new_set


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
