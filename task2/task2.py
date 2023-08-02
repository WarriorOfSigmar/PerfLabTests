import sys
import math

file_1 = sys.argv[1]
file_2 = sys.argv[2]

with open(file_1, "r") as file1:
    center = file1.readline().rstrip()
    center_x = center.split(" ")[0]
    center_y = center.split(" ")[1]
    radius = file1.readline().rstrip()

with open(file_2, "r") as file2:
    for line in file2:
        point = line.rstrip().split(" ")
        point_x = float(point[0]) - float(center_x)
        point_y = float(point[1]) - float(center_y)

        # hypotenuse formula
        formula = math.sqrt(point_x ** 2 + point_y ** 2)

        if formula < float(radius):
            print("1")
        elif formula == float(radius):
            print("0")
        else:
            print("2")
