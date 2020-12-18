from pathlib import Path

with open(f"{Path(__file__).parents[1]}/input") as problem_input:
    question_count = 0
    input_set = set()
    for person in problem_input:
        for question in person.strip():
            input_set.add(question)
        if person == "\n":
            question_count += len(input_set)
            input_set.clear()

print(question_count)