def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task5/tests/input', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

selection_sort(arr)

with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task5/tests/output', 'w') as f:
    f.write(' '.join(map(str, arr)))

