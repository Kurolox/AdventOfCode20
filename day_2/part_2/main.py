from pathlib import Path
import re

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    valid_passwords = 0
    pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    for line in problem_input:
        details = re.match(pattern, line)
        position_1, position_2 = int(details.group(1)), int(details.group(2))
        char_to_match, password = details.group(3), details.group(4)
        if (password[position_1-1] == char_to_match) ^ (password[position_2-1] == char_to_match):
            valid_passwords += 1

print(valid_passwords)
