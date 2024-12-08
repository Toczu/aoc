import pathlib
import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle.txt", "r")
lines = file.readlines()

antennas = dict()
town = []
for i in range(0, len(lines)):
    line = lines[i].strip()
    town.append(list(line))
    for j in range(0, len(line)):
        if line[j] != '.':
            key = line[j]
            if key in antennas.keys():
                antennas[key].append([i, j])
            else:
                antennas.update({ key: [[i, j]] })

town = np.array(town)
town_copy = np.copy(town)

print(town)
print(antennas)

overlap = set()
def create_antinode(q, p):
    global town
    global overlap
    global antennas
    # print(p, q)
    xd = q[0] - p[0]
    yd = q[1] - p[1]
    nx = p[0] - xd
    ny = p[1] - yd
    px = q[0] + xd
    py = q[1] + yd
    # print(f"distance {xd}, {yd}")
    # print(f"n coord {nx}, {ny}")
    # print(f"p coord {px}, {py}")
    while 0 <= nx < len(town) and 0 <= ny < len(town):
        town[nx, ny] = '#'
        # print(town)
        overlap.add((nx, ny))
        nx = nx + xd
        ny = ny + yd
        # print(nx, ny)
        # time.sleep(2)
        
    while 0 <= px < len(town) and 0 <= py < len(town):
        town[px, py] = '#'
        overlap.add((px, py))
        px = px + xd
        py = py + yd
    
    # print(town)


for key, values in antennas.items():
    if (len(values)) == 0:
        continue
    for i in range(0, len(values)):
        for j in range(0, len(values)):
            if i == j:
                continue
            create_antinode(values[i], values[j])

# print(overlap)
print(len(overlap))

s = 0
for i in range(0, len(town)):
    for j in range(0, len(town)):
        if town[i][j] == '#' and town_copy[i][j] != '.':
            town[i][j] = town_copy[i][j]
            s += 1

for i in range(0, len(town)):
    for j in range(0, len(town)):
        if town[i][j] == '#':
            s += 1

print(s)
print(town)