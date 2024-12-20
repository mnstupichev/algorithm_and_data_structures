from utils import read, write
from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

        return array


def main():
    array, = read()
    array = insertion_sort(array)
    write(*array)


if __name__ == "__main__":
    main()
