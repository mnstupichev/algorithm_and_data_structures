from utils import read, write
from collections import deque


def calculate_polish_notation(expression: list) -> int:
    stack = deque()
    for element in expression:
        if element in "+-*":
            num2 = stack.pop()
            num1 = stack.pop()
            result = None
            if element == '+':
                result = num1 + num2
            elif element == '-':
                result = num1 - num2
            elif element == '*':
                result = num1 * num2
            stack.append(result)
        else:
            stack.append(int(element))
    return stack.pop()


def main():
    expression, = read(type_convert=str)
    ans = calculate_polish_notation(expression)
    write(ans)


if __name__ == "__main__":
    main()
