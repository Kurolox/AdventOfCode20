from pathlib import Path
import re

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    valid_passwords = 0
    pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    for line in problem_input:
        details = re.match(pattern, line)
        min_amount, max_amount = int(details.group(1)), int(details.group(2))
        char_to_match, password = details.group(3), details.group(4)
        if min_amount <= password.count(char_to_match) <= max_amount:
            valid_passwords += 1

print(valid_passwords)
