import re

def part1(data):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, data)
    result = 0
    for match in matches:
        a, b = match.split(",")[1][:-1], match.split(",")[0][4:]
        result += int(a) * int(b)
    return result

def part2(data):
    mul_pattern = r"mul\(\d+,\d+\)"

    result = 0
    for match_obj in re.finditer(mul_pattern, data):
        match = match_obj.group()
        starting_index = match_obj.start(0)
        a, b = match.split(",")[1][:-1], match.split(",")[0][4:]

        do_dont = re.findall(r"(do|don't)\(\)", data[:starting_index])
        if not do_dont or do_dont[-1] == "do":
            result += int(a) * int(b)

    return result

if __name__ == "__main__":
    data = "".join(open("input.txt", "r").readlines())
    print(part1(data))

    data = "".join(open("input.txt", "r").readlines())
    print(part2(data))
