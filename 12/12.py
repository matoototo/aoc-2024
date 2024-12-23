from copy import deepcopy

class Node:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        # left up right down
        self.neighbors = [None, None, None, None]

    def valid_neighbors(self):
        return [n for n in self.neighbors if n and (n.type == self.type)]

    def __repr__(self):
        return f"{self.type}"

    def __hash__(self):
        return f"{self.x}-{self.y}".__hash__()

def flood_plot(node):
    plot = set()
    todo = [node]
    while todo:
        current = todo.pop(0)
        if current in plot: continue
        neighbors = current.valid_neighbors()
        todo.extend(neighbors)
        plot.add(current)
    return plot

def perimeter(plot):
    count = 0
    for node in plot:
        if node.type == "α": continue
        count += 4 - len(node.valid_neighbors())
    return count

def num_segments(border, for_x = True):
    possible = set([n.x for n in border])
    if not for_x: possible = set([n.y for n in border])
    count = 0
    for value in possible:
        on_that_val = [n for n in border if n.x == value]
        if not for_x: on_that_val = [n for n in border if n.y == value]
        max_val = max([n.y for n in on_that_val])
        max_val = max([max_val] + [n.x for n in on_that_val])
        layout = ["-" for _ in range(max_val+1)]
        for n in on_that_val:
            if for_x: layout[n.y] = "+"
            else: layout[n.x] = "+"
        layout = "".join(layout)
        count += len([seg for seg in layout.split("-") if seg])
    return count

def num_sides(plot):
    count = 0
    left_invalid = set()
    up_invalid = set()
    right_invalid = set()
    down_invalid = set()
    for node in plot:
        n = tuple(node.neighbors)
        left, up, right, down = n
        if left.type != node.type: left_invalid.add(left)
        if right.type != node.type: right_invalid.add(right)
        if up.type != node.type: up_invalid.add(up)
        if down.type != node.type: down_invalid.add(down)

    count += num_segments(left_invalid, False)
    count += num_segments(right_invalid, False)
    count += num_segments(up_invalid)
    count += num_segments(down_invalid)
    return count

def fencing_price(plot):
    perim = perimeter(plot)
    return perim * len(plot)

def fencing_price_p2(plot):
    n_sides = num_sides(plot)
    return n_sides * len(plot)

def part1(data):
    node_grid = parse_input(data)
    all_nodes = set(sum(node_grid, []))
    covered = set()
    plots = []
    for node in all_nodes:
        if node in covered or node.type == "α": continue
        plot = flood_plot(node)
        plots.append(plot)
        covered.update(plot)
    return sum(map(fencing_price, plots))

def part2(data):
    node_grid = parse_input(data)
    all_nodes = set(sum(node_grid, []))
    covered = set()
    plots = []
    for node in all_nodes:
        if node in covered or node.type == "α": continue
        plot = flood_plot(node)
        plots.append(plot)
        covered.update(plot)
    return sum(map(fencing_price_p2, plots))

def parse_input(data):
    node_grid = [list(x[:]) for x in data]
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            node_grid[i][j] = Node(i, j, c)

    for i, row in enumerate(node_grid[:-1]):
        for j, node in enumerate(row[:-1]):
            # up down
            next_row = node_grid[i+1]
            node.neighbors[3] = next_row[j]
            next_row[j].neighbors[1] = node

            # left right
            node.neighbors[2] = row[j+1]
            row[j+1].neighbors[0] = node

    last_row = node_grid[-1]
    for j, node in enumerate(last_row[:-1]):
        node.neighbors[2] = last_row[j+1]
        last_row[j+1].neighbors[0] = node

    last_column = [row[-1] for row in node_grid]
    for j, node in enumerate(last_column[:-1]):
        node.neighbors[3] = last_column[j+1]
        last_column[j+1].neighbors[1] = node

    return node_grid

if __name__ == "__main__":
    data = [x.strip() for x in open("input.txt", "r").readlines()]
    print(part1(data))

    data = [f"α{line}α" for line in data]
    data += ["α" * len(data[0])]
    data.insert(0, data[-1])
    print(part2(data))
