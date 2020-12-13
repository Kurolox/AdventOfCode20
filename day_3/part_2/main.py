from pathlib import Path
from math import prod

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    problem_input = problem_input.readlines()

trees_encountered = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for slope in slopes:
    slope_trees = 0
    for level, line in enumerate(problem_input):
        if level % slope[1] != 0:
            continue
        if line[(level//slope[1]*slope[0]) % len(line.strip())] == "#":
            slope_trees += 1
    trees_encountered.append(slope_trees)

print(prod(trees_encountered))
