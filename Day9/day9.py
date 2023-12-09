import re
import numpy as np

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

sequences = []
for line in lines:
    row = [int(m.group()) for m in re.finditer('-?\d+', line)]
    sequences.append(row)


def solve_part(sequences, part):
    # solution for part 1 is sum of last numbers
    # solution for part 2 is sum of first numbers with changing sign(eg. a-b+c-d...)
    counts = []
    for numbers in sequences:
        if part == 1:
            count = numbers[-1]
        else:
            sign = -1
            count = numbers[0]
        differences = numbers
        while 1:
            differences = np.diff(differences)
            if part == 1:
                count += differences[-1]
            else:
                count += differences[0] * sign
                sign = -sign
            if all(diff == 0 for diff in differences):
                break

        counts.append(count)
    return sum(counts)


print('Solution for part 1:', solve_part(sequences, 1))
print('Solution for part 2:', solve_part(sequences, 2))
