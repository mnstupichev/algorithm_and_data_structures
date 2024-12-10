from random import randint
from utils import time_data, memory_data
from lab4.task3.src.solution import check_right_brackets_sequence, main


def test_right_sequences():
    assert check_right_brackets_sequence('') == True
    assert check_right_brackets_sequence('()') == True
    assert check_right_brackets_sequence('((()))') == True
    assert check_right_brackets_sequence('[]') == True
    assert check_right_brackets_sequence('()[]') == True
    assert check_right_brackets_sequence('[(()[])[]((([][])))]') == True
    assert check_right_brackets_sequence('([])') == True
def test_invalid_sequences():
    assert check_right_brackets_sequence('(') == False
    assert check_right_brackets_sequence(']') == False
    assert check_right_brackets_sequence('[[))') == False
    assert check_right_brackets_sequence('(()()') == False
    assert check_right_brackets_sequence('())(') == False

def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
