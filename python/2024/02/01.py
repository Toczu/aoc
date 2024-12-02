import pathlib

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle_test.txt", "r")
lines = file.readlines()

reports = []

for line in lines:
    report = [int(i) for i in line.split()]
    safe = True
    inc = (report[0] - report[1]) > 0
    print(inc)
    for j in range(1, len(report)):
        print(f"{report[j-1]}, {report[j]}")
        diff = report[j-1] - report[j]
        if inc and diff < 0 and j != 1 or not inc and diff > 0 and j!= 1:
            safe = False
            break
        if  diff < 1 and diff > 3:
            safe = False
    reports.append(safe)

print(reports)
