if __name__ == '__main__':
    input_data = "data_challenge.in"
    # input_data = "data_test.in"

    DIRECTIONS: list[tuple[int, int]] = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    part1: int = 0
    part2: int = 0

    with (open(input_data, 'r') as f):
        map = f.read().splitlines()

        for idx_x, line in enumerate(map):
            for idx_y, char in enumerate(line):

                if char == "X":
                    for direction in DIRECTIONS:
                        do_count = True
                        for idx, letter in enumerate("MAS"):
                            new_x = idx_x + direction[0] * (idx + 1)
                            new_y = idx_y + direction[1] * (idx + 1)

                            if 0 <= new_x < len(map) and 0 <= new_y < len(map[new_x]) \
                                    and map[new_x][new_y] == letter:
                                continue

                            do_count = False
                            break

                        if do_count:
                            part1 += 1

                elif char == "A":
                    if 0 < idx_x < len(map) - 1 and 0 < idx_y < len(line) - 1:

                        if map[idx_x + 1][idx_y + 1] == "M" and map[idx_x - 1][idx_y - 1] == "S" \
                                or map[idx_x + 1][idx_y + 1] == "S" and map[idx_x - 1][idx_y - 1] == "M":

                            if map[idx_x + 1][idx_y - 1] == "M" and map[idx_x - 1][idx_y + 1] == "S" \
                                    or map[idx_x + 1][idx_y - 1] == "S" and map[idx_x - 1][idx_y + 1] == "M":
                                part2 += 1

    print("\n-- Part 1: --")
    print(part1)
    print("\n-- Part 2: --")
    print(part2)
