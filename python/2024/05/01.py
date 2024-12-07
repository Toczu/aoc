import pathlib
import numpy as np

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle_test.txt", "r")
lines = file.readlines()

rules = dict()
updates = []
change = False

for line in lines:
    if line == "\n":
        change = True
        continue
    
    if not change:
        l = [int(i) for i in line.strip().split('|')]
        key = l[0]
        if key in rules.keys():
            rules[key].append(l[1])
        else:
            rules.update({ l[0]: [l[1]] })
    else:
        updates.append([int(i) for i in line.strip().split(',')])

# [print(f"{k}: {v}") for k,v in rules.items()]
# [print(update) for update in updates]

correct_updates = []
for j in range(len(updates)):
    update = updates[j]
    correct = True
    # print(f'-- checking line {update} --')
    for i in range(len(update)):
        page = update[i]
        if page not in rules.keys():
            continue
        page_rules = rules[page]
        # print(page_rules)
        # print(np.isin(update, page_rules))
        # print(np.any(np.isin(update, page_rules)))
        # print(f"page {page}")
        # print(f"before {update[:i]}")
        # print(f"after {update[i+1:]}")
        if np.any(np.isin(update[:i], page_rules)):
            correct = False
    if correct:
        correct_updates.append(j)

sum = 0
for i in correct_updates:
    middle = int(len(updates[i]) / 2)
    sum += updates[i][middle]

print(sum)