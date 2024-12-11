from utils import read, write
from lab5.task4.src.solution import heapify


def heap_sort(array):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


def main():
    array, = read()
    heap_sort(array)
    write(*array)

if __name__ == '__main__':
    main()

if __name__ == "__main__":
    main()
