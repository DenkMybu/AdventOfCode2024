import re

mul_seq = r"mul\((\d{1,3}),(\d{1,3})\)"
seq = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
sum = 0
compute = True
with open('list.txt', 'r') as file:
    for line in file:
        print(line)
        list = re.finditer(seq, line)
        for item in list:
            output = item.group()
            print(output)
            if "don't()" in output:
                print("Turning it off because output = {}".format(output))
                compute = False
            if "do()" in output:
                print("Turning it on because output = {}".format(output))
                compute = True
            if compute and "mul" in output:
                found_seq = re.findall(mul_seq,output)
                print(found_seq)
                for _ in found_seq:
                    result = int(_[0]) * int(_[1])
                    print("{} * {}".format(int(_[0]),int(_[1])))
                    sum += result
           
                
print("Total sum of all multiplications: {}".format(sum))