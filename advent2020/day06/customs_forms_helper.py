import os


def read_file(filename: str) -> list:
    return open(os.path.join(os.path.dirname(__file__), filename)).read().split("\n\n")


def part1(groups: list) -> int:
    return sum([len(set(answers.replace("\n", ""))) for answers in groups])


def part2(groups: list) -> int:
    group_answers = [answers.splitlines() for answers in groups]
    for i, answers in enumerate(group_answers):
        for j, person in enumerate(answers):
            group_answers[i][j] = set(list(person))
    return sum(len(set.intersection(*group)) for group in group_answers)


def test():
    assert part1(read_file("input_test.txt")) == 11
    assert part2(read_file("input_test.txt")) == 6


if __name__ == "__main__":
    test()
    print("Part 1: ", part1(read_file("input.txt")))
    print("Part 2: ", part2(read_file("input.txt")))
