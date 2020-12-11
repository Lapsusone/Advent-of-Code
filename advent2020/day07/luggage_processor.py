import os
import re


def read_file(filename: str) -> list:
    return open(os.path.join(os.path.dirname(__file__), filename)).readlines()


def parse_bag(bag: str) -> dict:
    m = re.match("(.*) bags contain (.*).", bag)
    bag = {"color": m.group(1), "content": None}
    content = m.group(2).split(",")
    if not bag_is_empty(content):
        bag["content"] = parse_bag_content(content)
    print(bag)
    return bag


def bag_is_empty(bag_content: list) -> bool:
    return len(bag_content) == 1 and bag_content[0] == "no other bags"


def parse_bag_content(bag_content: list) -> list:
    r = re.compile("(\d+) (.*) bags?")
    return {
        r.match(content.strip()).group(2): int(r.match(content.strip()).group(1))
        for content in bag_content
    }


def part1(bags: list, color: str) -> int:
    return sum(
        part1(
            filter(
                lambda x: x["color"] in content.keys() and x["color"] is not color, bags
            ),
            color,
        )
        content.get(color)
        for content in [
            contained for contained in [bag.get("content") for bag in bags] if contained
        ]
    )


def test():
    file = read_file("input_test.txt")
    print(part1([parse_bag(bag) for bag in file], "shiny gold"))
    assert part1([parse_bag(bag) for bag in file], "shiny gold") == 4


if __name__ == "__main__":
    test()
