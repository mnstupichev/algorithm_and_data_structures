def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b % 10, a + b % 10
    return b % 10


with open("C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab0/task4/tests/input", "r") as input_file:
    data = input_file.readline()
n = int(data)

result = fib(n)

with open("C:/Users/Михаил/PycharmProjects/algorithm_and_data_structures/lab0/task4/tests/output", "w") as output_file:
    output_file.write(str(result))
