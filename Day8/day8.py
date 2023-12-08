import re
from math import lcm

network = []
dictionary = {}
with open('input.txt') as f:
    for line in f.readlines():
        nodes = []
        for m in re.finditer('\w+', line.strip()):
            nodes.append(m.group())
        if nodes:
            if len(nodes) == 1:
                instructions = nodes[0]
            else:
                network.append(nodes)
                dictionary[nodes[0]] = (nodes[1], nodes[2])


def part1(instructions, dictionary, start_node, end_node):
    count = 0
    while 1:
        for instruction in instructions:
            choice = dictionary[start_node]
            start_node = choice[0] if instruction == 'L' else choice[1]
            count += 1
            if start_node.endswith(end_node):
                return count


print('Solution for part 1:', part1(instructions, dictionary, 'AAA', 'ZZZ'))

start_nodes = [node for node in list(dictionary.keys()) if node.endswith('A')]
steps_counts = []
for node in start_nodes:
    steps_counts.append(part1(instructions, dictionary, node, 'Z'))

print('Solution for part 2:', lcm(*steps_counts))
