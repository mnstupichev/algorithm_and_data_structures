from utils import read, write
from typing import List


def binary_add(first_num: List[int], second_num:List[int]) -> List[int]:
    n = len(first_num)
    sum_result = [0] * (n + 1)
    extra = 0

    for i in range(n - 1, -1, -1):
        total = first_num[i] + second_num[i] + extra
        sum_result[i + 1] = total % 2
        extra = total // 2

    sum_result[0] = extra
    while len(sum_result) != 1 and sum_result[0] == 0:
        sum_result = sum_result[1:]
    return sum_result


def main():
    line, = read(type_convert=str)
    a_str, b_str = line[0], line[1]
    a = list(map(int, a_str))
    b = list(map(int, b_str))
    c = binary_add(a, b)
    write(*c, sep="")


if __name__ == "__main__":
    main()
