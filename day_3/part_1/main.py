from pathlib import Path

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    trees_encountered = 0
    for level, line in enumerate(problem_input):
        if line[(level*3) % len(line.strip())] == "#":
            trees_encountered += 1

print(trees_encountered)
