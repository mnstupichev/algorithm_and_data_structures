with open("/lab0/task2/textf/input", "r") as input_file:
    data = input_file.readline()

n = int(data)
result = 5 ** (-0.5) * (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n)

with open("/lab0/task2/textf/output", "w") as output_file:
    output_file.write(str(int(result)))
