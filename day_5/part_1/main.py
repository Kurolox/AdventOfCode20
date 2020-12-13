from pathlib import Path

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    highest_id = 0
    for line in problem_input:
        seat_row_low, seat_row_high = 0, 127
        seat_column_low, seat_column_high = 0, 7
        for i, char in enumerate(line.strip()):
            if i <= 6:
                new_point = (seat_row_low + seat_row_high) // 2
                if char == "F":
                    seat_row_high = new_point
                if char == "B":
                    seat_row_low = new_point
            else:
                new_point = (seat_column_low + seat_column_high) // 2
                if char == "R":
                    seat_column_low = new_point
                if char == "L":
                    seat_column_high = new_point
        if seat_row_high * 8 + seat_column_high > highest_id:
            highest_id = seat_row_high * 8 + seat_column_high

print(highest_id)
