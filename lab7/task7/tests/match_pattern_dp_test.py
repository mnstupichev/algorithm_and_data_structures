from utils import time_data, memory_data
from lab7.task7.src.solution import match_pattern_dp, main
from fnmatch import fnmatch


def test_set1():
    # given
    pattern = "k?t*n"
    string = "kitten"

    # when
    ans = match_pattern_dp(pattern, string)
    true_ans = fnmatch(string, pattern)

    # then
    assert true_ans == ans


def test_set2():
    # given
    pattern = "k?t?n"
    string = "kitten"

    # when
    ans = match_pattern_dp(pattern, string)
    true_ans = fnmatch(string, pattern)

    # then
    assert true_ans == ans


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
