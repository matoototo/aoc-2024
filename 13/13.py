class Configuration:
    def __init__(self, a, b, prize):
        self.a_x = a[0]
        self.a_y = a[1]
        self.b_x = b[0]
        self.b_y = b[1]
        self.prize = prize

    def cost_optimal_sol(self):
        target_x, target_y = self.prize[0], self.prize[1]
        min_cost = float("inf")
        for a_press in range(100):
            x, y = a_press * self.a_x, a_press * self.a_y
            cost = 3 * a_press
            needed_b_x = (target_x - x) / self.b_x
            needed_b_y = (target_y - y) / self.b_y
            valid_solution = needed_b_x == needed_b_y and needed_b_x.is_integer()
            if valid_solution:
                cost += needed_b_x
                min_cost = min(min_cost, cost)
        return min_cost

    def cost_optimal_direct(self):
        D = self.a_x * self.b_y - self.a_y * self.b_x
        if D == 0: return float("inf")
        n_a = self.prize[0] * self.b_y - self.prize[1] * self.b_x
        n_b = self.a_x * self.prize[1] - self.a_y * self.prize[0]
        a = n_a / D
        b = n_b / D
        if a < 0 or b < 0 or not a.is_integer() or not b.is_integer(): return float("inf")
        return 3 * a + b

def part1(data):
    configs = parse_input(data)

    total = 0
    for config in configs:
        cost = config.cost_optimal_sol()
        if cost == float("inf"): continue
        total += cost

    return int(total)

def part2(data):
    configs = parse_input(data, part2=True)

    total = 0
    for config in configs:
        cost = config.cost_optimal_direct()
        if cost == float("inf"): continue
        total += cost

    return int(total)


def parse_input(data, part2=False):
    configurations = data.split("\n\n")
    for i in range(len(configurations)):
        config = configurations[i].split("\n")
        a = [int(x[2:]) for x in config[0].split(": ")[1].split(", ")]
        b = [int(x[2:]) for x in config[1].split(": ")[1].split(", ")]
        extra = 10000000000000 if part2 else 0
        prize = [int(x[2:]) + extra for x in config[2].split(": ")[1].split(", ")]
        configurations[i] = Configuration(a, b, prize)

    return configurations

if __name__ == "__main__":
    data = open("input.txt", "r").read()
    print(part1(data))

    data = open("input.txt", "r").read()
    print(part2(data))
