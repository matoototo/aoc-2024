from copy import deepcopy


def parse_data(data):
    data = "".join(data).split('\n\n')
    assert len(data) == 2, f"Data invalid, assuming only 1 double newline (\\n\\n), found: {len(data) - 1}"
    grid = data[0].split("\n")
    moves = "".join(data[1].split("\n"))
    return grid, moves
    
def construct_set(grid, target):
    pairs = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != target: continue
            pairs.add((x, y))
    return pairs

def move_robot(robot, walls, boxes, move, is_box = False):
    deltas = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }
    delta = deltas[move]
    new_robot = (robot[0] + delta[0], robot[1] + delta[1])
    if new_robot in walls: return robot
    if new_robot in boxes:
        new_box = move_robot(new_robot, walls, boxes, move, is_box = True)
        if new_robot == new_box: return robot # immovable
        boxes.remove(new_robot)
    if is_box: boxes.add(new_robot)
    return new_robot

def expand_box(box):
    return [((box[0] - 1, box[1]), box), (box, (box[0] + 1, box[1]))]

def move_robot_p2(robot_or_box, walls, boxes, move, is_box = False, todo_add = None, todo_remove = None):
    if todo_add is None: todo_add = set()
    if todo_remove is None: todo_remove = set()
    deltas = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }
    delta = deltas[move]

    new_robot_or_box = []
    for robox in robot_or_box:
        new_robot = (robox[0] + delta[0], robox[1] + delta[1])
        new_robot_or_box.append(new_robot)
    new_robot_or_box = tuple(new_robot_or_box)

    if any(r in walls for r in new_robot_or_box): return robot_or_box
    box_queries = sum(map(expand_box, new_robot_or_box), [])
    overlapping = set([box for box in box_queries if box in boxes and box != robot_or_box])
    if overlapping:
        for box in overlapping:
            new_box = move_robot_p2(box, walls, boxes, move, is_box = True, todo_add = todo_add, todo_remove = todo_remove)
            if (box == new_box): return robot_or_box # immovable
        for box in overlapping:
            todo_remove.add(box)
    if is_box: todo_add.add(new_robot_or_box)
    else:
        for remove in todo_remove:
            boxes.remove(remove)
        for add in todo_add:
            boxes.add(add)
    return new_robot_or_box

def print_grid(walls, boxes, robot):
    grid = ""
    for y in range(1 + max([wall[0] for wall in walls])):
        for x in range(1 + max([wall[1] for wall in walls])):
            pos = (x, y)
            if pos in walls: grid += '#'
            elif pos in boxes: grid += 'O'
            elif pos == robot: grid += '@'
            else: grid += '.'
        grid += '\n'
    print(grid)
    
def print_grid_p2(walls, boxes, robot, width, height):
    grid = ""
    unwrapped_boxes = set(sum(([box[0], box[1]] for box in boxes), []))
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            if pos in walls: grid += '#'
            elif pos in unwrapped_boxes: grid += 'O'
            elif pos == robot: grid += '@'
            else: grid += '.'
        grid += '\n'
    print(grid)

def gps_coordinate(box):
    return box[0] + box[1] * 100

def gps_coordinate_p2(box):
    return gps_coordinate(box[0])

def part1(data):
    grid, moves = parse_data(data)
    walls = construct_set(grid, '#')
    boxes = construct_set(grid, 'O')
    robot = list(construct_set(grid, '@'))[0]
    for move in moves:
        robot = move_robot(robot, walls, boxes, move)
    print_grid(walls, boxes, robot)
    return sum(map(gps_coordinate, boxes))

def expand_grid(grid: list[str]):
    new_grid = []
    for line in grid:
        line = line.replace('.', '..')
        line = line.replace('#', '##')
        line = line.replace('O', '[]')
        line = line.replace('@', '@.')
        new_grid.append(line)
    return new_grid

def part2(data):
    grid, moves = parse_data(data)
    grid = expand_grid(grid)
    width = len(grid[0])
    height = len(grid)
    walls = construct_set(grid, '#')
    boxes_left = construct_set(grid, '[')
    boxes = set(((bl, (bl[0] + 1, bl[1])) for bl in boxes_left))
    robot = (list(construct_set(grid, '@'))[0],)

    for move in moves:
        robot = move_robot_p2(robot, walls, boxes, move)
    print_grid_p2(walls, boxes, robot[0], width, height)
    return sum(map(gps_coordinate_p2, boxes))

if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    print(part1(data))

    data = open("input.txt", "r").readlines()
    print(part2(data))
