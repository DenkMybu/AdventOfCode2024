with open('list.txt') as f:
        lines = [[int(x) for x in line.split()] for line in f]

def check_order(line):
    return all(line[i] < line[i + 1] for i in range(len(line) - 1)) or all(line[i] > line[i + 1] for i in range(len(line) - 1))

def check_diff(line):
    return all(1 <= abs(line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))

pass_check1_lines = [line for line in lines if check_order(line) and check_diff(line)]
#print(pass_check1_lines)
count = len(pass_check1_lines)
#print("Number of safe reports 1 = {}".format(count))

def count_with_remove(line):
    for i in range(len(line)):
        removed_val = line.pop(i)
        if check_order(line) and check_diff(line):
            line.insert(i,removed_val)
            return (True,i)
        line.insert(i,removed_val)
    return(False,None)

count_check2 = 0
count_firstrm = 0
for line in lines:
    passed_checks, idx_removed = count_with_remove(line)
    if passed_checks:
        print("Line {} is safe if {}th value is removed.".format(line,idx_removed))
        count_check2+=1
        if idx_removed == 0:
            count_firstrm+=1

print(count_check2)
print("There were {} events".format(len(lines)))
print("{}% of the total cases are safe passing first check".format((len(pass_check1_lines)*1.0/len(lines))*100))
print("{}% of the total cases are safe passing both checks".format((count_check2*1.0/len(lines)*100)))
print("{}% of the safe cases are safe when 0th value is removed".format((count_firstrm*1.0/count_check2)*100))
