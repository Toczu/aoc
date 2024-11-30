import pathlib

directory = str(pathlib.Path(__file__).parent.resolve()) + "/"

file = open(directory + "puzzle1_test.txt", "r")
lines = file.readlines()

for line in lines:
    print(line.strip())