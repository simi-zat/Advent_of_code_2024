import re


def multiply(command: str) -> int:
    nums: list[str] = re.findall(r'[0-9]+', command)
    return int(nums[0]) * int(nums[1])


if __name__ == '__main__':
    # input_data = "data_test_02.in"
    input_data = "data_challenge.in"

    part1: int = 0
    part2: int = 0
    enabled: bool = True
    instructions: list[tuple] = []

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            # print(line)

            instructions += [(f.start(), f.group()) for f in re.finditer(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)]
            instructions += [(f.start(), f.group()) for f in re.finditer(r'do\(\)', line)]
            instructions += [(f.start(), f.group()) for f in re.finditer(r'don\'t\(\)', line)]

            instructions.sort(key=lambda x: x[0])

            for instr in instructions:
                curr: str = instr[1]

                if curr.startswith("do("):
                    enabled = True
                elif curr.startswith("don"):
                    enabled = False
                else:
                    tmp = multiply(curr)
                    part1 += tmp
                    part2 += tmp if enabled else 0

    print("\n-- Part 1: --")
    print(part1)
    print("\n-- Part 2: --")
    print(part2)
