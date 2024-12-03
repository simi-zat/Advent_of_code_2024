if __name__ == '__main__':
    input_data: str = "data_challenge.in"

    left_list: list[int] = []
    right_list: list[int] = []
    distance: int = 0
    similarity: int = 0

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            values = line.split()
            left_list.append(int(values[0]))
            right_list.append(int(values[1]))

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])
        similarity += left_list[i] * right_list.count(left_list[i])

    print("\n-- Part 1: --")
    print(distance)
    print("\n-- Part 2: --")
    print(similarity)
