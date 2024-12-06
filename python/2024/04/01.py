import pathlib
import numpy as np
import re

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle_test.txt", "r")
lines = file.readlines()
sum = 0

def find_and_sum(line):
    global sum
    x = re.findall(r"XMAS", line)
    x2 = re.findall(r"SAMX", line)
    sum += len(x) + len(x2)

m = []

# vertical
for line in lines:
    l = line.strip()
    m.append(list(l))
    find_and_sum(l)

m = np.array(m)

# horizontal
for i in range(len(m)):
    l = ''.join(list(m[:, i]))
    find_and_sum(l)

# diagonal 1
for i in range(len(m) - 1, 0, -1):
    l = ''.join(list(m.diagonal(-i)))
    find_and_sum(l)
    print(l)
    
for i in range(len(m)):
    l = ''.join(list(m.diagonal(i)))
    find_and_sum(l)
    print(l)

# diagonal 2
m = np.fliplr(m)

for i in range(len(m) - 1, 0, -1):
    l = ''.join(list(m.diagonal(-i)))
    find_and_sum(l)
    print(l)
    
for i in range(len(m)):
    l = ''.join(list(m.diagonal(i)))
    find_and_sum(l)
    print(l)

print(sum)
