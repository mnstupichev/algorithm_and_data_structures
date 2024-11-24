def get_pallindrom(string):
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


with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task10/tests/input', 'r') as f:
    n = int(f.readline())
    string = f.readline().strip()

string = get_pallindrom(string)

with open('C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab1/task10/tests/output', 'w') as f:
    f.write(string)
