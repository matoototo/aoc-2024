from collections import defaultdict
from itertools import product

def get_antinodes(pair, repeating = False):
    first_node = pair[0]
    second_node = pair[1]

    x1, y1 = first_node
    x2, y2 = second_node

    dx, dy = x2 - x1, y2 - y1
    if not repeating: return set([(x2 + dx, y2 + dy), (x1 - dx, y1 - dy)])

    antinode_set = set()
    for i in range(0, 100):
        antinode_set.add((x2 + i*dx, y2 + i*dy))
        antinode_set.add((x1 - i*dx, y1 - i*dy))
    return antinode_set

def part1(data):
    antinodes = set()
    nodes = parse_input(data)
    max_x, max_y = len(data) - 1, len(data[0]) - 1
    for node_sets in nodes.values():
        pairs = product(node_sets, repeat=2)
        for pair in pairs:
            if pair[0] == pair[1]: continue
            antinodes.update(get_antinodes(pair))

    count_valid = 0
    for antinode in antinodes:
        x, y = antinode
        if x > max_x or x < 0: continue
        if y > max_y or y < 0: continue
        count_valid += 1

    return count_valid

def part2(data):
    antinodes = set()
    nodes = parse_input(data)
    max_x, max_y = len(data) - 1, len(data[0]) - 1
    for node_sets in nodes.values():
        pairs = product(node_sets, repeat=2)
        for pair in pairs:
            if pair[0] == pair[1]: continue
            antinodes.update(get_antinodes(pair, True))

    count_valid = 0
    for antinode in antinodes:
        x, y = antinode
        if x > max_x or x < 0: continue
        if y > max_y or y < 0: continue
        count_valid += 1

    return count_valid

def parse_input(data):
    nodes = defaultdict(set)
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == ".": continue
            nodes[c].add((i, j))
    return nodes

if __name__ == "__main__":
    data = [l.strip() for l in open("input.txt", "r").readlines()]
    print(part1(data))

    data = [l.strip() for l in open("input.txt", "r").readlines()]
    print(part2(data))
