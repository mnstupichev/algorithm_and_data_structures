from utils import read, write


def binary_add(A, B):
    n = len(A)
    C = [0] * (n + 1)
    extra = 0

    for i in range(n - 1, -1, -1):
        total = A[i] + B[i] + extra
        C[i + 1] = total % 2
        extra = total // 2

    C[0] = extra
    while len(C) != 1 and C[0] == 0:
        C = C[1:]
    return C


def main():
    line, = read(type_convert=str)
    a_str, b_str = line[0], line[1]
    a = list(map(int, a_str))
    b = list(map(int, b_str))
    c = binary_add(a, b)
    write(*c, sep="")


if __name__ == "__main__":
    main()
