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
        if valid_password(policy=policy):
            valid_passwords += 1
    return valid_passwords


def test():
    test_file = open(
        os.path.join(os.path.dirname(__file__), "input_test.txt")
    ).readlines()
    assert part1(test_file) == 2


if __name__ == "__main__":
    test()
    file = open(os.path.join(os.path.dirname(__file__), "input.txt")).readlines()
    print(f"Part 1: {part1(file)}")
