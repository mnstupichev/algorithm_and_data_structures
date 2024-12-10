from random import randint
from utils import time_data, memory_data
from lab3.task4.src.solution import points_in_section, points_in_section_naive, main


def test_from_task():
    sections = [(0, 5), (-3, 2), (7, 10)]
    points = [1, 3, 6]
    ans = points_in_section(sections, points)
    assert ans == [2, 1, 0]


def test_random_input():
    sections = []
    for _ in range(randint(1, 10000)):
        start = randint(-10**8, 10**8)
        end = randint(-10**8, 10**8)
        if start > end:
            start, end = end, start
        sections.append((start, end))

    points = []
    for _ in range(randint(1, 10000)):
        points.append(randint(-10**8, 10**8))
    points.sort()

    assert points_in_section_naive(sections, points) == points_in_section(sections, points)


def test_time():
    assert time_data(main) < 2


def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
