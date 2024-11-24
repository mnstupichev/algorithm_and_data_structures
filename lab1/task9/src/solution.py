def binary_add(A, B):
    n = len(A)
    C = [0] * (n + 1)
    extra = 0

    for i in range(n - 1, -1, -1):
        total = A[i] + B[i] + extra
        C[i + 1] = total % 2
        extra = total // 2

    C[0] = extra
    return C

with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task9/tests/input', 'r') as f:
    line = f.readline()
    A_str, B_str = line.split()
    A = list(map(int, A_str))
    B = list(map(int, B_str))

C = binary_add(A, B)

with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task9/tests/output', 'w') as f:
    f.write(''.join(map(str, C)))