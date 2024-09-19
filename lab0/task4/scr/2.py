from time import perf_counter

start_time = perf_counter()
with open("C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab0/task4/tests/input", "r") as input_file:
    data = input_file.readline()

n = int(data)
result = 5 ** (-0.5) * (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n)

with open("C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab0/task4/tests/output", "w") as output_file:
    output_file.write(str(int(result)) + "\n")
    output_file.write(str(perf_counter() - start_time))

