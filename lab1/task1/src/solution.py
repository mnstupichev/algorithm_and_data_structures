def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task1/tests/input', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

insertion_sort(arr)

with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task1/tests/output', 'w') as f:
    f.write(' '.join(map(str, arr)))
