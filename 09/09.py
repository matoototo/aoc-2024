def part1(data):
    data_blocks = [int(data[i]) for i in range(0, len(data), 2)]
    empty_blocks = [int(data[i]) for i in range(1, len(data), 2)]
    size_db = sum(data_blocks)

    i = 0
    block_idx = 0
    num_moved = 0
    last_block_idx = len(data_blocks) - 1

    result = []
    while i < size_db:
        db_len = data_blocks[block_idx]
        result += [block_idx] * db_len
        i += db_len
        if i >= size_db: break

        eb_len = empty_blocks[block_idx]
        num_moved = 0
        while num_moved < eb_len and last_block_idx > block_idx:
            last_block = data_blocks[last_block_idx]
            moved_len = min(last_block, eb_len - num_moved)
            result += [last_block_idx] * moved_len
            data_blocks[last_block_idx] -= moved_len
            if moved_len == last_block: last_block_idx -= 1
            num_moved += moved_len
        i += eb_len
        block_idx += 1

    r = 0
    for i, c in enumerate(result):
        r += i * int(c)
    return r

def part2(data):
    data_blocks = [int(data[i]) for i in range(0, len(data), 2)]
    empty_blocks = [int(data[i]) for i in range(1, len(data), 2)]

    result = []
    file_id = 0
    for fsize, esize in zip(data_blocks, empty_blocks):
        result.extend([file_id] * fsize)
        result.extend([-1] * esize)
        file_id += 1

    if len(data) % 2 == 1:
        last_file_size = int(data[-1])
        result.extend([file_id] * last_file_size)
        file_id += 1

    for block_idx in reversed(range(file_id)):
        positions = [i for i, block in enumerate(result) if block == block_idx]
        if not positions: continue

        file_len = len(positions)
        leftmost_pos = min(positions)

        best_start = None
        current_start = None
        current_length = 0

        for i in range(leftmost_pos):
            if result[i] == -1:
                if current_start is None: current_start = i
                current_length += 1
                continue

            if current_length >= file_len:
                best_start = current_start
                break
            current_start = None
            current_length = 0
        if current_start is not None and current_length >= file_len:
            best_start = current_start

        if best_start is not None:
            for pos in positions: result[pos] = -1
            for offset in range(file_len):
                result[best_start + offset] = block_idx

    r = 0
    for i, block in enumerate(result):
        if block != -1:
            r += i * block

    return r


if __name__ == "__main__":
    data = open("input.txt", "r").readlines()[0]
    print(part1(data))

    data = open("input.txt", "r").readlines()[0]
    print(part2(data))
