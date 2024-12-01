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

solution = np.sum(np.absolute(np.subtract(np.sort(ids_1), np.sort(ids_2))))

print(solution)
