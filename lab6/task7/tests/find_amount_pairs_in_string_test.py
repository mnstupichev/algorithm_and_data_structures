from utils import time_data, memory_data
from lab6.task7.src.solution import find_amount_pairs_in_string, main


def test_set1():
    # given
    string = "abacaba"
    beauty_pairs = {"a": ["a"]}

    # when
    result = find_amount_pairs_in_string(string, beauty_pairs)

    # then
    assert result == 6


def test_set2():
    # given
    string = "abacaba"
    beauty_pairs = {"b": ["a", "b"], "c": ["a"]}

    # when
    result = find_amount_pairs_in_string(string, beauty_pairs)

    # then
    assert result == 7


def test_time():
    # given
    time = time_data(main)

    # then
    assert time < 1


def test_memory_data():
    # given
    cur, peak = memory_data(main)

    # then
    assert cur < 64
    assert peak < 64