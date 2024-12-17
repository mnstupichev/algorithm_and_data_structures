from random import randint
from utils import time_data, memory_data
from lab4.task3.src.solution import check_right_brackets_sequence, main


def test_right_sequences():
    # given
    # when

    # then
    assert check_right_brackets_sequence('') == True
    assert check_right_brackets_sequence('()') == True
    assert check_right_brackets_sequence('((()))') == True
    assert check_right_brackets_sequence('[]') == True
    assert check_right_brackets_sequence('()[]') == True
    assert check_right_brackets_sequence('[(()[])[]((([][])))]') == True
    assert check_right_brackets_sequence('([])') == True


def test_invalid_sequences():
    # given
    # when

    # then
    assert check_right_brackets_sequence('(') == False
    assert check_right_brackets_sequence(']') == False
    assert check_right_brackets_sequence('[[))') == False
    assert check_right_brackets_sequence('(()()') == False
    assert check_right_brackets_sequence('())(') == False


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