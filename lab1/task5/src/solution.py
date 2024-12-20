from utils import read, write
from typing import List


def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


    return array

def main():
    array, = read()
    array = selection_sort(array)
    write(*array)


if __name__ == "__main__":
    main()

