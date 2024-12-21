class Node:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        # left up right down
        self.neighbors = [None, None, None, None]
        self.visited = self.type in "^<>v"

    def next_step(self, state):
        state_to_index = {'<': 0, '^': 1, '>': 2, 'v': 3}
        index_to_state = {0: '<', 1: '^', 2: '>', 3: 'v'}

        index = state_to_index[state]
        front_node = self.neighbors[index]

        if front_node is None: return None, None

        if front_node.type == '#':
            index = (index + 1) % 4
            return self, index_to_state[index]

        return front_node, state

    def __repr__(self):
        return self.type if not self.visited else "X"

def print_grid(node_grid):
    for row in node_grid:
        for node in row:
            print(node, end="")
        print("")
    print()

def walk(node, state):
    done_state_action = set()
    while True:
        key = f"{node.x}-{node.y}-{state}"
        if key in done_state_action: return True
        done_state_action.add(key)

        node.visited = True
        next_node, next_state = node.next_step(state)
        if not next_node: break
        node = next_node
        state = next_state
    return False

def is_loop(node, state, candidate):
    old_type = candidate.type
    candidate.type = '#'
    loops = walk(node, state)
    candidate.type = old_type
    return loops

def part1(data):
    node_grid = parse_input(data)
    node = [x for x in sum(node_grid, []) if x.type in "^<>v"][0]
    state = node.type
    walk(node, state)

    count = sum([1 for x in sum(node_grid, []) if x.visited])
    return count

def part2(data):
    node_grid = parse_input(data)
    node = [x for x in sum(node_grid, []) if x.type in "^<>v"][0]
    original_node = node
    state = node.type
    walk(node, state)

    candidates = [x for x in sum(node_grid, []) if x != original_node and x.type != "#"]
    loop_count = 0
    for candidate in candidates:
        node = original_node
        loop_count += is_loop(node, node.type, candidate)
    return loop_count

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

    print(part2(data))
