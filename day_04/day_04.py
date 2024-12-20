DIRECTIONS = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1)]

if __name__ == '__main__':
    input_data = "data_challenge.in"
    # input_data = "data_test.in"

    p1: int = 0
    p2: int = 0

    with open(input_data, 'r') as f:
        map = f.read().splitlines()

        for idx_x, line in enumerate(map):
            for idx_y, char in enumerate(map[idx_x]):

                if char == "X":
                    print(f"curr: {idx_x}, {idx_y} - {char}")

                    for direction in DIRECTIONS:
                        count = True
                        for idx, letter in enumerate("MAS"):
                            new_x = idx_x + direction[0] * (idx + 1)
                            new_y = idx_y + direction[1] * (idx + 1)

                            if 0 <= new_x < len(map) and 0 <= new_y < len(map[new_x]) and map[new_x][new_y] == letter:
                                continue

                            count = False
                            break

                        if count:
                            p1 += 1

    print("\n-- Part 1: --")
    print(p1)
    print("\n-- Part 2: --")
    print(p2)
