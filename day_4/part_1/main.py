from pathlib import Path
import re

passport_template = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False,
}

pattern = re.compile(r"(\w{3}):")

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    passport = passport_template.copy()
    valid_passports = 0
    for i, line in enumerate(problem_input):
        for field in re.findall(pattern, line):
            if field != "cid":
                passport[field] = True

        if line.startswith("\n"):
            if all(passport.values()):
                valid_passports += 1
            passport = passport_template.copy()

print(valid_passports)
