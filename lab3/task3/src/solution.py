from typing import List

from lab3.task1.src.solution import quick_sort
from utils import read, write


def fast_scarecrow_sort_check(array: List[int], k: int) -> bool:
    sorted_array = array[:]
    quick_sort(sorted_array)

    number_indexes = dict()
    for index, value in enumerate(array):
        if number_indexes.get(value) is None:
            number_indexes[value] = []

        number_indexes[value].append([index, False])


    for index, value in enumerate(sorted_array):
        for cur_index in number_indexes[value]:
            if not cur_index[1] and (cur_index[0] - index) % k == 0:
                cur_index[1] = True
                break
        else:
            return False

    return True


def naive_scarecrow_sort(array: List[int], k: int) -> bool:
    sorted_array = array[:]
    quick_sort(sorted_array)

    for i in range(k, len(array)):
        cur_index = i
        while cur_index - k >= 0 and array[cur_index - k] > array[cur_index]:
            array[cur_index - k], array[cur_index] = array[cur_index], array[cur_index - k]
            cur_index -= 1

    return sorted_array == array


def main():
    k,  array = list(read())
    k = k[0]
    if fast_scarecrow_sort_check(array, k):
        write("YES")
    else:
        write("NO")


if __name__ == "__main__":
    main()