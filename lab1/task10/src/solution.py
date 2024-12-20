from utils import read, write


def get_pallindrom(string: str) -> str:
    letters = set([let for let in string])
    count_letters = dict()
    for letter in letters:
        count_letters[letter] = string.count(letter)

    first_part = ""
    possible_middle_letter = []

    for let, count in count_letters.items():
        if count >= 2:
            first_part += let * (count // 2)
            if count % 2 == 1:
                possible_middle_letter.append(let)
        if count == 1:
            possible_middle_letter.append(let)

    if possible_middle_letter:
        possible_middle_letter.sort()
        middle_letter = possible_middle_letter[0]
    else:
        middle_letter = ''

    first_part = ''.join(sorted([let for let in first_part]))
    second_part = first_part[::-1]

    return first_part + middle_letter + second_part


def main():
    string, = read(type_convert=str)
    string = string[0]
    string = get_pallindrom(string)
    write(*string, sep="")


if __name__ == "__main__":
    main()
