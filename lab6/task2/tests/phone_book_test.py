from utils import time_data, memory_data
from lab6.task2.src.solution import PhoneBook, main
from random import randint, shuffle


def test_set():
    phonebook = PhoneBook()
    # given
    to_add = [(randint(10 ** 5, 10 ** 6 - 1), chr(randint(ord('a'), ord('z')))) for _ in range(10 ** 3)]

    for key, value in to_add:
        # when
        phonebook[key] = value

        # then
        assert value == phonebook[key]


def test_delete():
    # given
    phonebook = PhoneBook()
    to_add = [(randint(10 ** 5, 10 ** 6 - 1), chr(randint(ord('a'), ord('z')))) for _ in range(10 ** 3)]
    for key, value in to_add:
        phonebook[key] = value
    to_delete = [num for num, name in to_add]
    shuffle(to_delete)

    for key in to_delete:
        # when
        if key in phonebook:
            del phonebook[key]

            # then
            assert key not in phonebook


def test_time():
    # given
    time = time_data(main)

    # then
    assert time < 6


def test_memory_data():
    # given
    cur, peak = memory_data(main)

    # then
    assert cur < 512
    assert peak < 512
