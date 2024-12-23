class Node:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        # left up right down
        self.neighbors = [None, None, None, None]

    def valid_neighbors(self):
        return [n for n in self.neighbors if n and (n.type - self.type == 1)]

    def __repr__(self):
        return f"{self.type}"

    def __hash__(self):
        return f"{self.x}-{self.y}".__hash__()

def get_trail_score(head: Node):
    peaks = set()
    todo = [head]
    while todo:
        current = todo.pop(0)
        if current.type == 9:
            peaks.add(current)
            continue
        todo.extend(current.valid_neighbors())
    return len(peaks)

def get_trail_rating(head: Node):
    peaks = set()
    todo = [[head]]
    while todo:
        current_trail = todo.pop(0)[:]
        current = current_trail[-1]
        if current.type == 9:
            peaks.add(tuple(current_trail))
            continue
        todo.extend(current_trail + [x] for x in current.valid_neighbors())
    return len(peaks)

def part1(data):
    node_grid = parse_input(data)
    all_nodes = set(sum(node_grid, []))
    heads = [node for node in all_nodes if node.type == 0]
    return sum(get_trail_score(head) for head in heads)

def part2(data):
    node_grid = parse_input(data)
    all_nodes = set(sum(node_grid, []))
    heads = [node for node in all_nodes if node.type == 0]
    return sum(get_trail_rating(head) for head in heads)

def parse_input(data):
    node_grid = [list(x[:]) for x in data]
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            node_grid[i][j] = Node(i, j, int(c))

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

    print(part2(data))