def multiply_polynomials(a, b):
    n = len(a)
    if n == 1:
        return [a[0] * b[0]]

    m = n // 2
    a0 = a[:m]
    a1 = a[m:]
    b0 = b[:m]
    b1 = b[m:]

    z0 = multiply_polynomials(a0, b0)
    z2 = multiply_polynomials(a1, b1)
    z1 = multiply_polynomials(add_polynomials(a0, a1), add_polynomials(b0, b1))

    z1 = subtract_polynomials(z1, z0)
    z1 = subtract_polynomials(z1, z2)

    result = [0] * (2 * n - 1)
    for i in range(len(z0)):
        result[i] += z0[i]
    for i in range(len(z1)):
        result[i + m] += z1[i]
    for i in range(len(z2)):
        result[i + 2 * m] += z2[i]

    return result


def add_polynomials(a, b):
    max_len = max(len(a), len(b))
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))
    res = [0] * max_len
    for i in range(max_len):
        res[i] = a[i] + b[i]
    return res


def subtract_polynomials(a, b):
    max_len = max(len(a), len(b))
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))
    res = [0] * max_len
    for i in range(max_len):
        res[i] = a[i] - b[i]
    return res


with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab2/task8/tests/input', 'r') as f:
    n = int(f.readline())
    koef_first_polynomial = list(map(int, f.readline().split()))
    koef_second_polynomial = list(map(int, f.readline().split()))

ans = multiply_polynomials(koef_first_polynomial, koef_second_polynomial)

with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab2/task8/tests/output', 'w') as f:
    f.write(' '.join(map(str, ans)))
