import itertools

def evaluate(arguments, operators):
    result = arguments[0]
    for i, (arg, op) in enumerate(zip(arguments[1:], operators)):
        if not op: result += arg
        elif op == 1: result *= arg
        elif op == 2: result = int(f"{result}{arg}")
    return result

def possibly_true(candidate, with_concat = False):
    result, arguments = candidate[0], candidate[1]
    # 0 -> +, 1 -> product, 2 -> concat
    all_operators = [0, 1, 2] if with_concat else [0, 1]
    operators_list = itertools.product(all_operators, repeat=len(arguments)-1)
    for operators in operators_list:
        if evaluate(arguments, operators) == result: return True
    return False

def part1(data):
    candidates = parse_input(data)
    return sum([c[0] for c in candidates if possibly_true(c)])

def part2(data):
    candidates = parse_input(data)
    return sum([c[0] for c in candidates if possibly_true(c, True)])

def parse_input(data):
    candidates = []
    for line in data:
        split = line.split(": ")
        result = int(split[0].strip())
        arguments = list(map(int, split[1].strip().split(" ")))
        candidates.append((result, arguments))
    return candidates

if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    print(part1(data))

    data = open("input.txt", "r").readlines()
    print(part2(data))
