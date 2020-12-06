bin_seat_codes = []
import math

with open('problem5/input.txt', 'r') as file:
    bin_seat_codes = file.read().splitlines()


def get_row(bin_code):
    row_info = bin_code[:7]

    bottom_row = 0
    top_row = 127

    for char in row_info:
        print(bottom_row, top_row)

        distance = int((top_row - bottom_row + 1) / 2)
        if char == "F":
            top_row -= distance
        elif char == "B":
            bottom_row += distance

    if bottom_row != top_row:
        raise Exception(f"Invalid code {bin_code}")

    return bottom_row

def get_col(bin_code):
    left_col = 0
    right_col = 7
    col_info = bin_code[7:]

    for char in col_info:
        print(left_col, right_col)

        distance = int((right_col - left_col + 1) / 2)
        if char == "L":
            right_col -= distance
        elif char == "R":
            left_col += distance

    if left_col != right_col:
        raise Exception(f"Invalid code {bin_code}")

    return left_col


def calculate_seat_id(row, col):
    return row * 8 + col


def solve_part_one():
    """
    Determine the largest Seat ID
    """
    largest_seat_id = -1
    for code in bin_seat_codes:
        row_num = get_row(code)
        col_num = get_col(code)
        seat_id = calculate_seat_id(row_num, col_num)

        if seat_id > largest_seat_id:
            largest_seat_id = seat_id


    print(f"Largest seat ID: {largest_seat_id}")


def solve_part_two():
    # Only store seats not in the front or back.
    seat_id_bins = {}
    for code in bin_seat_codes:
        row_num = get_row(code)
        col_num = get_col(code)
        seat_id = calculate_seat_id(row_num, col_num)

        if seat_id < 127 * 8 and seat_id >= 8:
            # Valid potential seating location
            seat_id_bins[seat_id] = code

    sorted_ids = list(seat_id_bins.keys())
    sorted_ids.sort()
    for idx in range(len(sorted_ids)):
        seat_id = sorted_ids[idx]
        if sorted_ids[idx +1 ] == sorted_ids[idx] + 2:
            # We found the skipped seat
            print(f"Your seat: {sorted_ids[idx] + 1}")
            break





def test_input():
    code = "FBFBBFFRLR"
    row_num = get_row(code)
    col_num = get_col(code)

    seat_id = calculate_seat_id(row_num, col_num)

    print("Final results")
    print(row_num, col_num, seat_id)



solve_part_one()
solve_part_two()
# test_input()
