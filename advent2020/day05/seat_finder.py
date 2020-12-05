import os


def read_file(filename: str) -> str:
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


def parse_boarding_pass(boarding_pass: str) -> tuple:
    assert len(boarding_pass) == 10
    return find_row(boarding_pass[:7]), find_column(boarding_pass[-3:])


def get_seat_id(boarding_pass: str) -> int:
    row, column = parse_boarding_pass(boarding_pass)
    return row * 8 + column


def find_row(row_descriptor: str) -> int:
    assert len(row_descriptor) == 7
    return int(row_descriptor.replace("F", "0").replace("B", "1"), 2)


def find_column(column_descriptor: str) -> int:
    assert len(column_descriptor) == 3
    return int(column_descriptor.replace("R", "1").replace("L", "0"), 2)


def find_highest_seat_id(input: list) -> int:
    max_seat_id = 0
    for boarding_pass in input:
        seat_id = get_seat_id(boarding_pass)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def find_my_seat_id(input: list) -> int:
    seats_sequence = sorted(get_seat_id(b_pass) for b_pass in input)
    for i, seat in enumerate(seats_sequence):
        if seats_sequence[i + 1] != seat + 1:
            return seat + 1


def test():
    file = read_file("input_test.txt").splitlines()
    assert find_highest_seat_id(file) == 820


if __name__ == "__main__":
    test()
    file = read_file("input.txt").splitlines()
    print("Part 1: ", find_highest_seat_id(file))
    print("Part 2: ", find_my_seat_id(file))
