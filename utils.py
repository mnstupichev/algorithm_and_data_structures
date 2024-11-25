def write_file(file_path, data):
    f2 = open(file_path, 'w')
    if not isinstance(data, list) and str(abs(data)).isdigit():
        f2.write(str(data))
    elif '\n' in data[0]:
        f2.write(("").join(list(map(str, data))))
    else:
        f2.write((" ").join(list(map(str, data))))

    f2.close()


def read_data(file_path: str):
    file = open(file_path, 'r')
    lines = file.readlines()
    data = []
    i = 0
    while i < len(lines):
        line = lines[i]

        if len(line.split()) == 1:
            try:
                data.append(int(line))
            except ValueError:
                data.append(line)
        else:
            try:
                data.append(list(map(int, line.split())))
            except ValueError:
                data.append(line.split())
        i += 1
    file.close()
    return data


def print_end_test(time, amount_data):
    print('Время работы: %s секунд' % time)
    print("Память:", amount_data, "МБ")


def print_task_data(tasknum, inp, output):
    print(f"task {tasknum}")
    print("input: " + str(inp))
    print("output: " + str(output) + "\n")