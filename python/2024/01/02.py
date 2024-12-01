import pathlib
import numpy as np

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle.txt", "r")
lines = file.readlines()

ids_1 = []
ids_2 = []

for line in lines:
    l = line.split()
    ids_1.append(int(l[0]))
    ids_2.append(int(l[1]))

a1 = dict()
for i in ids_2:
    if i in a1.keys():
        a1[i] += 1
    else:
        a1[i] = 1

solution = 0
for i in ids_1:
    if i in a1.keys():
        solution += i * a1[i]

print(solution)