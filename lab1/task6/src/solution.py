from utils import read, write


def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def main():
    array, = read()
    bubble_sort(array)
    write(*array)


if __name__ == "__main__":
    main()
