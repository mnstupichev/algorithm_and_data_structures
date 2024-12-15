from typing import Callable, List, Tuple
from utils import read, write


class PhoneBook:
    def __init__(self, capacity: int = 10 ** 6, hash_func: Callable = hash):
        self.capacity: int = capacity
        self.hash_func: Callable = hash_func
        self.buckets: List[List[Tuple[int, str]]] = [[] for _ in range(self.capacity)]

    def get_bucket(self, key: int) -> List[Tuple[int, str]]:
        bucket_ind = self.hash_func(key) % self.capacity
        return self.buckets[bucket_ind]

    def __getitem__(self, key: int) -> str:
        bucket = self.get_bucket(key)
        for cur_key, cur_val in bucket:
            if cur_key == key:
                return cur_val

    def __setitem__(self, key: int, value: str) -> None:
        bucket = self.get_bucket(key)
        for i, (cur_key, cur_val) in enumerate(bucket):
            if cur_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def __delitem__(self, key: int) -> None:
        bucket = self.get_bucket(key)
        for i, (cur_key, _) in enumerate(bucket):
            if cur_key == key:
                del bucket[i]
                return

    def __contains__(self, key: int) -> bool:
        is_contain = False
        for cur_key, _ in self.get_bucket(key):
            if cur_key == key:
                is_contain = True
                break
        return is_contain

    def __iter__(self):
        for bucket in self.buckets:
            for pair in bucket:
                yield pair


def main():
    phone_book = PhoneBook()
    *commands, = read(type_convert=str)
    write(end="")

    for command, *values in commands:
        if command == "add":
            phone_book[values[0]] = values[1]
        elif command == "del":
            del phone_book[values[0]]
        elif command == "find":
            if values[0] in phone_book:
                write(phone_book[values[0]], to_end=True)
            else:
                write("not found", to_end=True)


if __name__ == "__main__":
    main()
