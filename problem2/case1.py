with open('list.txt') as f:
        lines = [[int(x) for x in line.split()] for line in f]

def check_order(line):
    return all(line[i] < line[i + 1] for i in range(len(line) - 1)) or all(line[i] > line[i + 1] for i in range(len(line) - 1))

def check_diff(line):
    return all(1 <= abs(line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))

pass_check1_lines = [line for line in lines if check_order(line) and check_diff(line)]
print(pass_check1_lines)

count = len(pass_check1_lines)
print("Number of safe reports = {}".format(count))
