with open("C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab0/task1/tests/input", "r") as input_file:
    data = input_file.readline()

a, b = map(int, data.split())

with open("C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab0/task1/tests/output", "w") as output_file:
    output_file.write(str(a + b ** 2))