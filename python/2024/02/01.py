import pathlib
import numpy as np

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle.txt", "r")
lines = file.readlines()

reports = []

for line in lines:
    report = [int(i) for i in line.split()]
    safe = True
    inc = report[0] < report[1]
    for j in range(1, len(report)):
        diff = report[j-1] - report[j]
        if inc and diff > 0 or not inc and diff < 0:
            safe = False
            break
        diff = abs(diff)
        if diff == 0:
            safe = False
            break
        if not (diff >= 0 and diff <= 3):
            safe = False
            break
    reports.append(safe)

print(reports)
print(np.array(reports).sum())
