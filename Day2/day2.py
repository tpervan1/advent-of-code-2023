import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

count1, count2 = 0, 0
for line in lines:
    # lists with numbers and first letter of color
    positions = [[int(m.group()), line[m.end() + 1]] for m in re.finditer('\d+', line)]
    for game in positions:
        # games are impossible if r>12, g>13 or b>14
        if (game[1] == 'r' and game[0] > 12) or (game[1] == 'g' and game[0] > 13) or (game[1] == 'b' and game[0] > 14):
            count1 += positions[0][0]
            break

    reds = list(filter(lambda x: x[1] == 'r', positions))
    greens = list(filter(lambda x: x[1] == 'g', positions))
    blues = list(filter(lambda x: x[1] == 'b', positions))
    a, b, c = max(reds)[0], max(greens)[0], max(blues)[0]
    count2 += a * b * c

# game's id is increasing by 1
print('Solution for part 1:', sum(range(len(lines) + 1)) - count1)
print('Solution for part 2:', count2)
