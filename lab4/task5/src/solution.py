from utils import read, write
from collections import deque


class MaxStack:
    def __init__(self):
        self.stack = deque()
        self.cur_max = float('-inf')

    def push(self, value: int):
        self.stack.append((value, self.cur_max))
        if self.cur_max < value:
            self.cur_max = value

    def pop(self):
        last, last_max = self.stack.pop()

        if last == self.cur_max:
            self.cur_max = last_max
        return last

    def max(self):
        if len(self.stack) == 0:
            raise IndexError
        return self.cur_max


def main():
    stack = MaxStack()
    write(end="")
    for line in read(type_convert=str):
        if line[0] == 'push':
            stack.push(int(line[1]))
        elif line[0] == 'pop':
            stack.pop()
        elif line[0] == 'max':
            write(stack.max(), to_end=True)


if __name__ == '__main__':
    main()
