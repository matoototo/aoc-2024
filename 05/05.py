from collections import defaultdict

def update_valid(before_map, update):
    for i, before in enumerate(update):
        for after in update[i:]:
            if before in before_map[after]: return False
    return True

def find_swap(before_map, update):
    for i, before in enumerate(update):
        for j, after in enumerate(update[i:]):
            if before in before_map[after]:
                return [i, i+j]
    return None

def fix_update(before_map, update):
    swaps = []
    while (swap := find_swap(before_map, update)):
        i, j = swap[0], swap[1]
        update[i], update[j] = update[j], update[i]
    return update

def iter_closure(before_map: dict):
    new_before_map = defaultdict(set)
    for before, after_set in before_map.items():
        new_before_map[before] = after_set.copy()
        for after in after_set:
            if after not in before_map: continue
            new_before_map[before].update(before_map[after].copy())
    return new_before_map

def part1(rules, updates):
    before_map = defaultdict(set) # key must be before all values
    for rule in rules:
        before, after = rule[0], rule[1]
        before_map[before].add(after)

    # while True:
    #     new_before_map = iter_closure(before_map)
    #     if new_before_map == before_map: break
    #     before_map = new_before_map

    sum = 0
    for update in updates:
        if not update_valid(before_map, update): continue
        sum += update[len(update) // 2]
    return sum

def part2(rules, updates):
    before_map = defaultdict(set) # key must be before all values
    for rule in rules:
        before, after = rule[0], rule[1]
        before_map[before].add(after)

    sum = 0
    for update in updates:
        if update_valid(before_map, update): continue
        fixed_update = fix_update(before_map, update)
        sum += fixed_update[len(fixed_update) // 2]
    return sum

def parse_input(data):
    rules_str = data.split("\n\n")[0].strip().split("\n")
    updates_str = data.split("\n\n")[1].strip().split("\n")

    rules = [[int(x) for x in rule.split("|")] for rule in rules_str]
    updates = [[int(x) for x in update.split(",")] for update in updates_str]

    return rules, updates

if __name__ == "__main__":
    data = open("input.txt", "r").read()
    rules, updates = parse_input(data)
    print(part1(rules, updates))

    data = open("input.txt", "r").read()
    rules, updates = parse_input(data)
    print(part2(rules, updates))
