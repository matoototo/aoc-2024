from collections import Counter

def part1(first, second):
    distance_sum = sum(abs(a - b) for a, b in zip(first, second))
    return distance_sum

def part2(first, second):
    counted = Counter(second)
    total_score = 0
    for number in first:
        if number not in counted: continue
        total_score += counted[number]*number
    return total_score


if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    data = [line.strip() for line in data]

    first = sorted([int(line.split()[0]) for line in data])
    second = sorted([int(line.split()[1]) for line in data])

    print(part1(first, second))
    print(part2(first, second))
