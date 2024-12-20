from typing import Callable, List
from utils import read, write


class Set:
    def __init__(self, capacity: int = 10 ** 5, hash_func: Callable = hash):
        self.capacity = capacity
        self.hash_func: Callable = hash_func
        self.buckets: List[List[int]] = [[] for _ in range(self.capacity)]

    def get_bucket(self, value: int) -> List[int]:
        bucket_ind = self.hash_func(value) % self.capacity
        return self.buckets[bucket_ind]

    def add(self, value: int) -> None:
        bucket = self.get_bucket(value)

        if value not in bucket:
            bucket.append(value)

    def remove(self, value: int) -> None:
        bucket = self.get_bucket(value)

        if value in bucket:
            bucket.remove(value)
        else:
            raise ValueError(f"Number {value} not found.")

    def __contains__(self, value: int) -> bool:
        return value in self.get_bucket(value)

    def __iter__(self):
        for bucket in self.buckets:
            for value in bucket:
                yield value


def main():
    *commands, = read(type_convert=str)
    custom_set = Set()
    write(end="")

    for command, value in commands:
        if command == "A":
            custom_set.add(value)
        elif command == "D":
            custom_set.remove(value)
        elif command == "?":
            if value in custom_set:
                write("Y", to_end=True)
            else:
                write("N", to_end=True)


if __name__ == "__main__":
    main()
