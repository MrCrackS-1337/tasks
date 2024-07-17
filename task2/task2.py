import sys
from math import pow

def readlines_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()

circle_data = readlines_file(sys.argv[1])
points_data = readlines_file(sys.argv[2])

cx = float(circle_data[0].split()[0])
cy = float(circle_data[0].split()[1])
r = float(circle_data[1])
r2 = pow(r, 2)

for line in points_data:
    px = float(line.split()[0])
    py = float(line.split()[1])
    
    v = pow(px - cx, 2) + pow(py - cy, 2)
    
    if v > r2:
        print(2)
    elif v == r2:
        print(0)
    else:
        print(1)
