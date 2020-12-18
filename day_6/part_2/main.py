from pathlib import Path
from itertools import groupby

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    question_count = 0
    # resulting_list = list of lists, each list is a group that contains each person choice as a set
    # i.e. two groups: three persons (a, b, c) and two persons (abc, ad)
    # resulting_list = [[{a}, {b}, {c}], [{a, b, c}, {a, d}]]
    resulting_list = [list(group) for key, group in groupby(
        [set(list(person.rstrip())) for person in problem_input.readlines()], lambda x: x != set()) if key]

for group in resulting_list:
    if len(group) == 1:
        question_count += len(group[0])
    else:
        question_count += len(group[0].intersection(*group[1:]))

print(question_count)
