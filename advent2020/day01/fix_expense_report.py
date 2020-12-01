import os

dirname = os.path.dirname(__file__)
lines = [int(x[:-1]) for x in open(os.path.join(dirname, "input.txt"), "r").readlines()]


def part1(input):
    for a in input:
        if (2020 - a) in input:
            return (2020 - a) * a


def part2(input):
    for a in input:
        for b in input:
            if (2020 - a - b) in input:
                return (2020 - a - b) * a * b


def test():
    lines = [
        int(x[:-1])
        for x in open(os.path.join(dirname, "input_test.txt"), "r").readlines()
    ]
    assert part1(lines) == 514579
    assert part2(lines) == 241861950


if __name__ == "__main__":
    test()
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
