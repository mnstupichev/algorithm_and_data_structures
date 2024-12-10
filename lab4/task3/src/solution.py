from utils import read, write
from collections import deque


def check_right_brackets_sequence(brackets: str):
    stack = deque()
    for bracket in brackets:
        if bracket in ')]':
            if len(stack) == 0:
                return False

            last = stack.pop()
            if bracket == ')' and last == '[' or bracket == ']' and last == '(':
                return False
        else:
            stack.append(bracket)

    if len(stack) != 0:
        return False
    return True


def main():
    brackets_list = list(read(type_convert=str))
    write("", end="")
    for brackets in brackets_list:
        if check_right_brackets_sequence(brackets[0]):
            write('YES', to_end=True)
        else:
            write('NO', to_end=True)


if __name__ == '__main__':
    main()

if __name__ == "__main__":
    main()
