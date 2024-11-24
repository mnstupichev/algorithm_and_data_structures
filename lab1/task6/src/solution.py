def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task6/tests/input', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

bubble_sort(arr)

with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task6/tests/output', 'w') as f:
    f.write(' '.join(map(str, arr)))
