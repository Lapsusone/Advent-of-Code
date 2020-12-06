import os


def read_file(filename: str) -> list:
    file = open(os.path.join(os.path.dirname(__file__), filename)).read().split("\n\n")
    return [line.replace("\n", "") for line in file]


def part1(groups: list) -> int:
    return sum([len(set(answers)) for answers in groups])


def test():
    assert part1(read_file("input_test.txt")) == 11


if __name__ == "__main__":
    test()
    print("Part 1: ", part1(read_file("input.txt")))
