from typing import List, Tuple
from utils import read, write


def heapify(array: List[int], array_len: int, cur_ind: int) -> None:
    largest = cur_ind
    left = 2 * cur_ind + 1
    right = 2 * cur_ind + 2

    if left < array_len and array[largest] < array[left]:
        largest = left

    if right < array_len and array[largest] < array[right]:
        largest = right

    if largest != cur_ind:
        array[cur_ind], array[largest] = array[largest], array[cur_ind]

        heapify(array, array_len, largest)


def min_heapify(array: List[int], array_len: int, cur_ind: int, swaps: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    least = cur_ind
    left = 2 * cur_ind + 1
    right = 2 * cur_ind + 2

    if left < array_len and array[least] > array[left]:
        least = left

    if right < array_len and array[least] > array[right]:
        least = right

    if least != cur_ind:
        array[cur_ind], array[least] = array[least], array[cur_ind]
        swaps.append((cur_ind, least))

        min_heapify(array, array_len, least, swaps)

    return swaps


def heap_executing(array: List[int]) -> List[Tuple[int, int]]:
    n = len(array)
    m, swaps = 0, []
    for i in range(n // 2, -1, -1):
        cur_swaps = min_heapify(array, n, i, [])
        for swap in cur_swaps:
            swaps.append(swap)

    return swaps


def main():
    array, = read()
    swaps = heap_executing(array)
    write(len(swaps))
    for swap in swaps:
        write(*swap, to_end=True)


if __name__ == '__main__':
    main()
