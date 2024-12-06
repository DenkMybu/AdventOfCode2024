import re

mul_seq = r"mul\((\d{1,3}),(\d{1,3})\)"
sum = 0

with open('list.txt', 'r') as file:
    for line_number, line in enumerate(file):
        found_seq = re.findall(mul_seq, line)
        for _ in found_seq:
            result = int(_[0]) * int(_[1])
            sum += result
            print("Found 'mul({},{})' on line {}".format(int(_[0]),int(_[1]),line_number))
            

    print("Total sum of all multiplications: {}".format(sum))
