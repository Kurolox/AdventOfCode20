from pathlib import Path

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    input_set = set()
    for line in problem_input:
        input_set.add(int(line))

for x in input_set:
    for y in input_set:
        for z in input_set:
            if x + y + z == 2020:
                print(x*y*z)
                exit()
