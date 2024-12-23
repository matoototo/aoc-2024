from collections import Counter, defaultdict

def evolve_stone(stone):
    strnum = str(stone)
    if stone == 0: return (1,)
    if not len(strnum) % 2:
        a, b = strnum[:len(strnum) // 2], strnum[len(strnum) // 2:]
        return (int(a), int(b))
    return (stone * 2024,)

def evolve_stones(stones: Counter):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        for new_stone in evolve_stone(stone):
            new_stones[new_stone] += count
    return new_stones

def part1(stones: set):
    stones = stones.copy()
    for i in range(25):
        stones = evolve_stones(stones)
    return sum(stones.values())

def part2(stones):
    stones = stones.copy()
    for i in range(75):
        stones = evolve_stones(stones)
    return sum(stones.values())

if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    stones = Counter(map(int, data[0].strip().split()))
    print(part1(stones))

    data = open("input.txt", "r").readlines()
    stones = Counter(map(int, data[0].strip().split()))
    print(part2(stones))
