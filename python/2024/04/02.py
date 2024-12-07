import pathlib
import numpy as np

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle.txt", "r")
lines = file.readlines()

# M.S  -1,-1   -1, +1
# .A.        X
# M.S  +1,-1   +1, +1

m = []

# vertical
for line in lines:
    l = line.strip()
    m.append(list(l))

sum = 0
m = np.array(m)
for k in range(4):
    for i in range(1, len(m) -1):
        for j in range(1, len(m[:,]) - 1):
            # print(i, j)
            # print(m[i][j], m[i-1][j-1], m[i-1][j+1])
            if m[i][j] == 'A' and m[i-1][j-1] == 'M' and m[i-1][j+1] == 'S' and m[i+1][j-1] == 'M' and m[i+1][j+1] == 'S':
                sum += 1
                # print('asd')
    m = np.rot90(m)
            
print(sum)