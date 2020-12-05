import os
import re


def parse_passport(passport: str):
    passport = passport.strip().replace("\n", " ").split(" ")
    passport_dict = {}

    for field in passport:
        field_key, field_value = field.split(":")
        passport_dict[field_key] = field_value
    return passport_dict


def is_valid_passport(passport: dict):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(field in passport.keys() for field in required_fields)


def validate(input_):
    return sum(is_valid_passport(parse_passport(passport)) for passport in input_)


def is_valid_passport_2(passport: dict):
    return is_valid_passport(passport) and all(
        is_valid_field(field, passport[field]) for field in passport.keys()
    )


def is_valid_field(field: str, value: str):
    if field == "byr":
        return 1920 <= int(value) <= 2002
    elif field == "iyr":
        return 2010 <= int(value) <= 2020
    elif field == "eyr":
        return 2020 <= int(value) <= 2030
    elif field == "hgt":
        height, unit = re.search(r"(\d+)(\w+)", value).groups()
        return (
            unit == "cm"
            and 150 <= int(height) <= 193
            or unit == "in"
            and 59 <= int(height) <= 76
        )
    elif field == "hcl":
        return bool(re.fullmatch(r"#[0-9a-f]{6}", value))
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return bool(re.fullmatch(r"\d{9}", value))
    elif field == "cid":
        return True
    else:
        return False


def validate_2(input_):
    return sum(is_valid_passport_2(parse_passport(passport)) for passport in input_)


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
