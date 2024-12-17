from utils import time_data, memory_data
from lab5.task1.src.solution import check_heap, main


def test_set_1():
    # given
    array = [1, 0, 1, 2, 0]

    # when
    # Nothing to do here

    # then
    assert check_heap(array) == False


def test_set_2():
    # given
    array = [1, 3, 2, 5, 4]

    # when
    # Nothing to do here

    # then
    assert check_heap(array) == True


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
