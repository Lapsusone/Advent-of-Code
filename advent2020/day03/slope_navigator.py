import os


def navigate(input, right, down):
    lines = input.splitlines()
    height = len(lines)
    width = len(lines[0])
    tree_count = 0
    y = 0
    x = 0
    while y < height:
        if lines[y][x] == "#":
            tree_count += 1
        x = (x + right) % width
        y += down
    return tree_count


def part2(input):
    total = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        total *= navigate(input, right, down)
    return total


def test():
    file = open(os.path.join(os.path.dirname(__file__), "input_test.txt")).read()
    assert navigate(file, 3, 1) == 7
    assert navigate(file, 1, 1) == 2
    assert navigate(file, 5, 1) == 3
    assert navigate(file, 7, 1) == 4
    assert navigate(file, 1, 2) == 2
    assert part2(file) == 336


if __name__ == "__main__":
    test()
    file = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(f"Part 1: {navigate(file, 3, 1)}")
    print(f"Part 2: {part2(file)}")
