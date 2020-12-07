import string
groups = []




# Consume the file and build a list of groups
with open('problem6/input.txt', 'r') as file:
    raw_data = file.readlines()
    group = []

    for entry in raw_data:
        # Build a list of all groups.
        if entry == "\n":
            groups.append(group)
            group = []
        else:
            group.append(entry.rstrip())

    groups.append(group)


def solve_problem_one(groups):
    """
    For each group calculate its "yes" responses.
    """
    total_group_yes_responses = 0
    total_universal_group_yes_responses = 0

    group_response_sets = []

    print(f"{len(groups)} groups")
    for group in groups:
        group_responses = set()
        universal_agreeing_answers = set(string.ascii_lowercase)
        for response in group:
            # print(set(response))
            response = set(response)
            universal_agreeing_answers = universal_agreeing_answers.intersection(response)
            group_responses = group_responses.union(response)
        total_group_yes_responses += len(group_responses)
        total_universal_group_yes_responses += len(universal_agreeing_answers)
        group_response_sets.append(group_responses)

    print(total_group_yes_responses)
    print(total_universal_group_yes_responses)


def solve_problem_two(groups):
    pass

solve_problem_one(groups)
