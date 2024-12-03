import pathlib
import numpy as np

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle_test.txt", "r")
lines = file.readlines()

reports = []

# for line in lines:
#     report = [int(i) for i in line.split()]
#     safe = True
#     inc = report[len(report)-1] - report[0] > 0
#     r = 0
#     print(report)
#     for j in range(1, len(report)):
#         diff = report[j] - report[j-1]
#         print(f"inc {inc}")
#         print(f"diff {diff}")
#         if inc and diff < 0 or not inc and diff > 0:
#             print(f'asd {j}')
#             safe = False
#             print(f"len {len(report) - 1}")
#             if j < len(report) - 1:
#                 k = j-1
#                 print(f"k {k}")
#                 l = abs(report[k-1] - report[k+1])
#                 print(f"l {l}")
#                 if l < 3 and l > 0:
#                     print("rplus")
#                     safe = True
#         diff = abs(diff)
#         if diff == 0:
#             safe = False
#             r += 1
#         if not (abs(diff) > 0 and abs(diff) < 4):
#             print(f'j {j}, {len(report) - 1}')
#             safe = False
#             print(f"j {j}")
#             k = j-1
#             print(f"k {k}")
#             l = abs(report[k-1] - (report[k+1] or 0))
#             print(f"l {l}")
#             if l <= 3 and l > 0:
#                 print("rplus")
#                 safe = True
#     print(f"r {r}")
#     if r == 1:
#         safe = True
#     reports.append(safe)

# print(reports)
# print(np.array(reports).sum())

for line in lines:
    report = [int(i) for i in line.split()]
    inc = report[len(report) - 1] - report[0] > 0
    diff = np.diff(report)
    print(report)
    print()

a = []
# for report in reports:
#     safe = True
#     for i in range(len(report) - 1):
#         if diff > 3 or diff == 0:
#             ix = i + 2
#             if ix > len(report) - 1:
#                 ix = len(report) - 1
#             d = (report[ix]) - report[i]
#             if d < 4 and d > 0:
#                 safe = True
#             else:
#                 safe = False
#     a.append(safe)

# print(a)
# print(np.array(a).sum())