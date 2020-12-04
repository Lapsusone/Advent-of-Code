import os
import re


def parse_passport(passport: list):
    passport = passport.replace("\n", " ").rsplit(" ")
    passport_dict = {}
    for field in passport:
        (field_key, _, field_value) = field.partition(":")
        passport_dict[field_key] = field_value
    return passport_dict


def is_valid_passport(passport: dict):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(field in passport.keys() for field in required_fields):
        return True
    return False


def validate(input):
    valid = 0
    for passport in input:
        pp = parse_passport(passport)
        if is_valid_passport(pp):
            valid += 1
    return valid


def is_valid_passport_2(passport: dict):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(field in passport.keys() for field in required_fields):
        return all(is_valid_field(field, passport[field]) for field in passport.keys())
    return False


def is_valid_field(field: str, value: str):
    if field == "byr":
        return int(value) >= 1920 and int(value) <= 2002
    elif field == "iyr":
        return int(value) >= 2010 and int(value) <= 2020
    elif field == "eyr":
        return int(value) >= 2020 and int(value) <= 2030
    elif field == "hgt":
        m = re.search("(\d+)(\w+)", value)
        if m.group(2) == "cm":
            return int(m.group(1)) >= 150 and int(m.group(1)) <= 193
        elif m.group(2) == "in":
            return int(m.group(1)) >= 59 and int(m.group(1)) <= 76
        else:
            return False
    elif field == "hcl":
        return re.fullmatch("#[0-9a-f]{6}", value) is not None
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return re.fullmatch("\d{9}", value) is not None
    else:
        return False


def validate_2(input):
    valid = 0
    for passport in input:
        pp = parse_passport(passport)
        if is_valid_passport_2(pp):
            valid += 1
    return valid


def test():
    input = (
        open(os.path.join(os.path.dirname(__file__), "input_test.txt"))
        .read()
        .split("\n\n")
    )
    assert validate(input) == 2


if __name__ == "__main__":
    test()
    input = (
        open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split("\n\n")
    )
    print(f"Part 1: {validate(input)}")
    print(f"Part 2: {validate_2(input)}")
