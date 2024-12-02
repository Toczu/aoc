import pathlib

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle_test.txt", "r")
lines = file.readlines()

reports = []

for line in lines:
    report = [int(i) for i in line.split()]
    safe = True
    print(report)
    inc = report[0] < report[1]
    for j in range(1, len(report)):
        print(f"{report[j-1]}, {report[j]}")
        diff = report[j-1] - report[j]
        print(diff)
        if not (diff >= 0 and diff <= 3) and j!= 1:
            safe = False
            break
    print(f"aaa {safe}")
    reports.append(safe)

print(reports)

