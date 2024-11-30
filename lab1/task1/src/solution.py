from utils import read, write


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    array, = read()
    insertion_sort(array)
    write(*array)


if __name__ == "__main__":
    main()
