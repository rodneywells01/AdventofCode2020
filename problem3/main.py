TREE = "#"
lines = None
with open('problem3/input.txt', 'r') as f:
    lines = f.read().splitlines()


def slide_down_hill(slope, hill):
    l_index = 0
    vertical_index = 0
    trees_hit = 0
    while vertical_index < len(hill):
        # Handle wrapping of the hill
        if l_index >= len(hill[vertical_index]):
            l_index -= len(hill[vertical_index])

        # Did we hit a tree?
        if hill[vertical_index][l_index] == TREE:
            trees_hit += 1

        # Slide down the hill
        vertical_index += slope[1]
        l_index += slope[0]

    return trees_hit


def solve_part_one():
    print(slide_down_hill([3,1], lines))

def solve_part_two():

    slope_trajectories = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    results = []
    running_mul_total = 1
    for trajectory in slope_trajectories:
        running_mul_total *= slide_down_hill(trajectory, lines)

    print(running_mul_total)





solve_part_one()
solve_part_two()
