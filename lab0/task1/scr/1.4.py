with open("/lab0/task1/textf/input", "r") as input_file:
    data = input_file.readline()

a, b = map(int, data.split())

with open("/lab0/task1/textf/output", "w") as output_file:
    output_file.write(str(a + b ** 2))