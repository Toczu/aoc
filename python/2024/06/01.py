import pathlib
import time
import numpy as np
import os

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle.txt", "r")
lines = file.readlines()

matrix = []
m, n = 0, 0
direction = 'UP'
go = True

for i in range(len(lines)):
    l = list(lines[i].strip())
    matrix.append(l)
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            m, n = i, j
try:
    while go:
        # os.system('cls' if os.name == 'nt' else 'clear')
        matrix[m][n] = 'X'
        if direction == 'UP':
            if matrix[m - 1][n] != '#':
                m -= 1
            else:
                direction = 'RIGHT'
                n += 1
        elif direction == 'DOWN':
            if matrix[m + 1][n] != '#':
                m += 1
            else:
                direction = 'LEFT'
        elif direction == 'RIGHT':
            if matrix[m][n + 1] != '#':
                n += 1
            else:
                direction = 'DOWN'    
        elif direction == 'LEFT':
            if matrix[m][n - 1] != '#':
                n -= 1
            else:
                direction = 'UP'
        matrix[m][n] = 'X'
        if m < 0 or m > len(matrix[0]):
            go = False
        if n < 0 or n > len(matrix):
            go = False
        print(direction)        
        print(np.array(matrix))
        # time.sleep(1)

except:
    print()

sum = 0
for line in matrix:
    for l in line:
        if l == 'X':
            sum += 1

print(sum)