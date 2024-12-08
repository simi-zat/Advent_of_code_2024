import re




def multiply(command: str) -> int:
    nums: list[str] = re.findall(r'[0-9]+', command)
    return int(nums[0]) * int(nums[1])




if __name__ == '__main__':
    # input_data = "data_test.in"
    input_data = "data_challenge.in"

    part1: int = 0
    part2: int = 0


    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            print(line)


            xx = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
            print(xx)


            for x in xx:
                part1 += multiply(x)

            # break



    print("\n-- Part 1: --")
    print(part1)
    print("\n-- Part 2: --")
    print(part2)



