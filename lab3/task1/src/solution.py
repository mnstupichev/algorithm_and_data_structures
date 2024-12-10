from utils import read, write
from random import randint
from typing import List, Tuple


def partition(array: List, start: int, end: int) -> Tuple[int, int]:
    pivot = array[randint(start, end - 1)]
    end_less_part = end_equal_part = start
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[end_equal_part], array[end_less_part] = array[end_equal_part], array[end_less_part], array[i]
            end_less_part += 1
            end_equal_part += 1
        elif array[i] == pivot:
            array[end_equal_part], array[i] = array[i], array[end_equal_part]
            end_equal_part += 1

    return end_less_part, end_equal_part


def quick_sort(array: List, start: int = 0, end: int = -1) -> None:
    if end == -1:
        end = len(array)

    if end - start <= 1:
        return

    end_less_part, end_equal_part = partition(array, start, end)
    quick_sort(array, start, end_less_part)
    quick_sort(array, end_equal_part, end)


def main():
    array, = read()
    quick_sort(array)
    write(*array)


if __name__ == "__main__":
    main()
