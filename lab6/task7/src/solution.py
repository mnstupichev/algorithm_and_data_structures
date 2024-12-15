from typing import Dict, List
from utils import read, write


def find_amount_pairs_in_string(string: str, beauty_pairs: Dict[str, List[str]]):
    counter = [0 for _ in range(26)]
    ans = 0
    for let in string:
        if let in beauty_pairs.keys():
            for first_el in beauty_pairs.get(let):
                ans += counter[ord(first_el) - ord('a')]
        counter[ord(let) - ord('a')] += 1

    return ans


def main():
    (string,), *pairs = read(type_convert=str)
    beauty_pairs = dict()
    for pair in pairs:
        pair = pair[0]
        first_el, second_el = pair[0], pair[1]
        if second_el not in beauty_pairs.keys():
            beauty_pairs[second_el] = []
        beauty_pairs[second_el].append(first_el)

    ans = find_amount_pairs_in_string(string, beauty_pairs)

    write(ans)


if __name__ == '__main__':
    main()