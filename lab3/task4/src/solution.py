from typing import List, Tuple

from lab3.task1.src.solution import quick_sort
from utils import read, write



def points_in_section(sections: List[Tuple[int, int]], points: List[int]):
    main_array = []

    for section in sections:
        main_array.append((section[0], 0))
        main_array.append((section[1], 2))

    for point in points:
        main_array.append((point, 1))

    quick_sort(main_array)

    cur = 0
    ans = []
    for point in main_array:
        if point[1] == 0:
            cur += 1
        elif point[1] == 1:
            ans.append(cur)
        elif point[1] == 2:
            cur -= 1
    return ans


def points_in_section_naive(sections: List[Tuple[int, int]], points: List[int]):
    ans = []
    for point in points:
        count = 0
        for start, end in sections:
            if start <= point <= end:
                count += 1
        ans.append(count)
    return ans


def main():
    *sections, points = list(read())
    write(*points_in_section(sections, points))


if __name__ == "__main__":
    main()