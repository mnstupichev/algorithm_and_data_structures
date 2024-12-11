from utils import time_data, memory_data
from lab5.task1.src.solution import check_heap, main

def test_set_1():
    array = [1, 0, 1, 2, 0]
    assert check_heap(array) == False


def test_set_2():
    array = [1, 3, 2, 5, 4]
    assert check_heap(array) == True


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
