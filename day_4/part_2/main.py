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

pattern = re.compile(r"(\w{3}):(#?\w+)")

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    passport = passport_template.copy()
    valid_passports = 0
    for i, line in enumerate(problem_input):
        for field in re.findall(pattern, line):
            if field[0] == "byr":
                if 1920 <= int(field[1]) <= 2002:
                    passport[field[0]] = True
            elif field[0] == "iyr":
                if 2010 <= int(field[1]) <= 2020:
                    passport[field[0]] = True
            elif field[0] == "eyr":
                if 2020 <= int(field[1]) <= 2030:
                    passport[field[0]] = True
            elif field[0] == "hgt":
                if field[1][-2:] == "cm" and 150 <= int(field[1].split("cm")[0]) <= 193:
                    passport[field[0]] = True
                elif field[1][-2:] == "in" and 59 <= int(field[1].split("in")[0]) <= 76:
                    passport[field[0]] = True
            elif field[0] == "ecl":
                if field[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    passport[field[0]] = True
            elif field[0] == "pid":
                if re.match(re.compile(r"\d{9}$"), field[1]):
                    passport[field[0]] = True
            elif field[0] == "hcl":
                if re.match(re.compile(r"#([a-fA-F0-9]){6}$"), field[1]):
                    passport[field[0]] = True
        if line.startswith("\n"):
            if all(passport.values()):
                valid_passports += 1
            print(f"passport {i}: {passport}")
            passport = passport_template.copy()

print(valid_passports)
