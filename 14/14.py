from functools import partial
from collections import Counter
from math import ceil, prod


class Robot:
    def __init__(self, init_str: str):
        self.initialize(init_str)

    def initialize(self, init_str: str):
        init_str = init_str.strip().split(" ")
        pos, vel = init_str[0][2:].split(","), init_str[1][2:].split(",")
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.vx = int(vel[0])
        self.vy = int(vel[1])

    def __repr__(self):
        return f"p={self.x},{self.y} v={self.vx},{self.vy}"

def iterate(iters: int, robot: Robot):
    robot.x += iters * robot.vx
    robot.y += iters * robot.vy
    return robot

def contain(width: int, height: int, robot: Robot):
    robot.x %= width
    robot.y %= height
    return robot

def print_grid(width: int, height: int, robots: list[Robot]):
    grid = []
    for y in range(height):
        for x in range(width):
            length = len(list(filter(lambda r : (r.x == x and r.y == y), robots)))
            grid.append(str(length))
    output = ""
    for start in range(0, width * height, width):
        output += "".join(grid[start:start+width])
        output += '\n'
    print(output)

def print_contain_iter(width: int, height: int, robots: list[Robot], iter: int):
    robots = map(partial(iterate, 1), robots)
    robots = list(map(partial(contain, width, height), robots))
    # signal -> lots at one X (is edge)
    y_counts = Counter(robot.y for robot in robots)
    max_count = max(y_counts.values())
    if max_count > 30:
        print("Iteration: ", iter, "\n")
        print_grid(width, height, robots)
        print(f"\n{'*'*100}\n")
    return robots

def quadrantize(width: int, height: int, robot: Robot):
    x, y = robot.x, robot.y
    if x == width // 2 or y == height // 2:
        return -1
    quadrant = 0
    if x > width // 2: quadrant += 1
    if y > height // 2: quadrant += 2
    return quadrant

def part1(data, width = 101, height=103, iters=100):
    robots = map(Robot, data)
    robots = map(partial(iterate, iters), robots)
    robots = list(map(partial(contain, width, height), robots))
    quadrants = map(partial(quadrantize, width, height), robots)
    counts = Counter(quadrants)
    return prod([counts for q, counts in counts.items() if q != -1])

def part2(data, width = 101, height=103):
    robots = map(Robot, data)
    for i in range(10000):
        robots = print_contain_iter(width, height, robots, i)


if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    print(part1(data))

    data = open("input.txt", "r").readlines()
    print(part2(data))
