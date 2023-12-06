import re
from functools import reduce
from math import sqrt


def solve_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    return (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)


with open('input.txt') as f:
    lines = [m.group() for line in f.readlines() for m in re.finditer('\d+', line.strip())]

numbers = [int(line) for line in lines]
times, distances = numbers[0:int(len(numbers) / 2)], numbers[int(len(numbers) / 2): len(numbers)]

count = 0
counts = []
for i, time in enumerate(times):
    for secs in range(0, time + 1):
        if (time - secs) * secs > distances[i]:
            count += 1
    counts.append(count)
    count = 0

print('Solution for part 1: ', reduce((lambda x, y: x * y), counts))
# -----------------------------------------
times, distances = lines[0:int(len(lines) / 2)], lines[int(len(lines) / 2): len(lines)]
time = int(reduce((lambda x, y: x + y), times))
distance = int(reduce((lambda x, y: x + y), distances))

# brute force
# count = 0
# for secs in range(0, time + 1):
#    result = (time - secs) * secs
#    if result > distance:
#        count += 1
# print(count)

x1, x2 = solve_quadratic_equation(-1, time, -distance)
print('Solution for part 2: ', int(x2) - int(x1))
