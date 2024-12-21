def is_safe(sequence):
    sequence = list(sequence)
    if len(sequence) <= 1: return True
    increasing, decreasing, small_gap = True, True, True
    for x, y in zip(sequence, sequence[1:]):
        small_gap *= abs(x - y) <= 3
        increasing *= y > x
        decreasing *= x > y
    return (increasing or decreasing) and small_gap

def part1(data):
    return sum(map(is_safe, data[:]))

def part2(data):
    safe_reports = 0
    for report in data:
        report = list(report)
        safe_reports += any(is_safe(report[:i] + report[i+1:]) for i in range(len(report))) or is_safe(report)
    return safe_reports


if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    data = [map(int, line.strip().split()) for line in data]
    print(part1(data))

    data = open("input.txt", "r").readlines()
    data = [map(int, line.strip().split()) for line in data]
    print(part2(data))
