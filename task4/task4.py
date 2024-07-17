import sys
import math

def readlines_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()

numbers = [int(n) for n in readlines_file(sys.argv[1])]

avg = 0
for n in numbers:
    avg += n
avg/= len(numbers)

avg_ceil = math.ceil(avg)
avg_floor = math.floor(avg)

def calculate_steps(numbers, target):
    steps = 0
    for n in numbers:
        steps += abs(n - target)
    return steps

v1 = calculate_steps(numbers, avg_ceil)
v2 = calculate_steps(numbers, avg_floor)

print(min(v1, v2))
