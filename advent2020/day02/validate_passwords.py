import os
import re


def valid_password(policy):
    n_occurences = policy["password"].count(policy["character"])
    return (
        n_occurences >= policy["minOccurences"]
        and n_occurences <= policy["maxOccurences"]
    )


def part1(input):
    valid_passwords = 0
    for line in input:
        m = re.search("(\d+)-(\d+) (\w): (.+)", line)
        policy = {
            "minOccurences": int(m.group(1)),
            "maxOccurences": int(m.group(2)),
            "character": m.group(3),
            "password": m.group(4),
        }
        if valid_password(policy):
            valid_passwords += 1
    return valid_passwords


def valid_password_part2(policy):
    return (
        policy["password"][policy["pos1"] - 1] == policy["character"]
        and policy["password"][policy["pos2"] - 1] != policy["character"]
        or policy["password"][policy["pos1"] - 1] != policy["character"]
        and policy["password"][policy["pos2"] - 1] == policy["character"]
    )


def part2(input):
    valid_passwords = 0
    for line in input:
        m = re.search("(\d+)-(\d+) (\w): (.+)", line)
        policy = {
            "pos1": int(m.group(1)),
            "pos2": int(m.group(2)),
            "character": m.group(3),
            "password": m.group(4),
        }
        if valid_password_part2(policy):
            valid_passwords += 1
    return valid_passwords


def test():
    test_file = open(
        os.path.join(os.path.dirname(__file__), "input_test.txt")
    ).readlines()
    assert part1(test_file) == 2
    assert part2(test_file) == 1


if __name__ == "__main__":
    test()
    file = open(os.path.join(os.path.dirname(__file__), "input.txt")).readlines()
    print(f"Part 1: {part1(file)}")
    print(f"Part 2: {part2(file)}")
