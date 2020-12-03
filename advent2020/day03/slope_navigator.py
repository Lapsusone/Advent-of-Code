import os


def navigate(input, right, down):
    lines = input.read().splitlines()
    height = len(lines)
    width = len(lines[0])
    tree_count = 0
    i = 1
    while i < height:
        index = i * right % width
        if lines[i - 1 + down][index] == "#":
            tree_count += 1
        i += 1
    return tree_count


def test():
    file = open(os.path.join(os.path.dirname(__file__), "input_test.txt"))
    assert navigate(file, 3, 1) == 7


if __name__ == "__main__":
    test()
    file = open(os.path.join(os.path.dirname(__file__), "input.txt"))
    print(f"Part 1: {navigate(file, 3, 1)}")
