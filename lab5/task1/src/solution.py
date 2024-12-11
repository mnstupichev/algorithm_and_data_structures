from typing import List
from utils import read, write


def check_heap(array: List[int]) -> bool:
    for i in range(1, len(array)):
        if array[(i + 1) // 2 - 1] > array[i]:
            return False
    return True


def main():
    array, = read()
    if check_heap(array):
        write("YES")
    else:
        write("NO")


if __name__ == '__main__':
    main()
