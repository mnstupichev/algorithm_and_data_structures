from collections import deque
from utils import read, write


def main():
    commands = read(type_convert=str)
    write("", end="")
    stack = deque()
    for command in commands:
        if command[0] == '+':
            stack.append(command[1])
        elif command[0] == '-':
            write(stack.pop(), to_end=True)


if __name__ == '__main__':
    main()