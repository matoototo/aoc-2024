import re

def transpose(data):
    transposed = ["" for i in range(len(data[0]))]
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            transposed[j] += c
    return transposed

def mirror(data):
    return [x[::-1] for x in data]

def count_horizontal(data):
    joined_data = ".".join(data)
    return len(re.findall("XMAS", joined_data))

def count_horizontal_mas(data):
    count = 0
    for i, row in enumerate(data[:-2]):
        for j, c in enumerate(row[:-2]):
            if c != "M" or row[j+2] != "M": continue
            if data[i+1][j+1] != "A": continue
            if data[i+2][j] != "S" or data[i+2][j+2] != "S": continue
            count += 1
    return count

def count_diag(data):
    count = 0
    for i, row in enumerate(data[:-3]):
        for j, c in enumerate(row[:-3]):
            if c != "X": continue
            match = f"{c}{data[i+1][j+1]}{data[i+2][j+2]}{data[i+3][j+3]}"
            count += match == "XMAS"
    return count

def tranpose_and_mirror(data):
    variants = [data]
    variants.append(transpose(variants[-1]))
    variants.append(mirror(variants[-1]))
    variants.append(mirror(variants[0]))
    return variants

def flip_and_mirror(data):
    variants = [data]
    variants.append(variants[-1][::-1])
    variants.append(mirror(variants[-1]))
    variants.append(mirror(variants[0]))
    return variants

def all_rotations(data):
    variants = [data]
    variants.append(variants[-1][::-1]) # 180
    variants.append(transpose(variants[0])[::-1]) # 270
    variants.append(transpose(variants[0]))
    return variants

def part1(data):
    horizontal_count = sum([count_horizontal(variant) for variant in tranpose_and_mirror(data)])
    diag_count = sum([count_diag(variant) for variant in flip_and_mirror(data)])
    return horizontal_count + diag_count

def part2(data):
    horizontal_count = sum([count_horizontal_mas(variant) for variant in all_rotations(data)])
    return horizontal_count

if __name__ == "__main__":
    data = [x.strip() for x in open("input.txt", "r").readlines()]
    print(part1(data))

    data = [x.strip() for x in open("input.txt", "r").readlines()]
    print(part2(data))
