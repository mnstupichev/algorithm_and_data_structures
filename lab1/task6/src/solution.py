from utils import read, write
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def main():
    array, = read()
    array = bubble_sort(array)
    write(*array)


if __name__ == "__main__":
    main()
