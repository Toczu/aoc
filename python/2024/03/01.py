import pathlib
import re

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle.txt", "r")
lines = file.readlines()

sum = 0
for line in lines:
    l = line.strip()
    x = re.findall(r"mul\([0-9]*,[0-9]*\)", l)
    for m in x:
        n = re.findall(r"[0-9]*", m)
        k = [int(i) for i in n if i.isdecimal()]
        sum += k[0] * k[1]

print(sum)