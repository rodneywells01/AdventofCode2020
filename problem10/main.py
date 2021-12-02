# Read input
with open('problem10/input.txt', 'r') as file:
    joltage_adapters = file.read().splitlines()
    for idx in range(len(joltage_adapters)):
        joltage_adapters[idx] = int(joltage_adapters[idx])

joltage_adapters.sort()
print(joltage_adapters)


one_difference = 0
three_difference = 1 # Built in adapter always is +3

joltage = 0

for adapter in joltage_adapters:
    diff = adapter - joltage
    if diff == 1:
        one_difference += 1
    elif diff == 3:
        three_difference += 1
    elif diff > 3:
        raise Exception("We're fucked")

    joltage = adapter

print(one_difference)
print(three_difference)
print(one_difference * three_difference)


def solve_num_connections(idx, joltage):
    if joltage_adapters[idx] - joltage > 3:
        return 0

    if joltage_adapters[idx] == joltage:
        return 1

    next_three_idx = 1
    total_connections = 0
    joltage = joltage_adapters[idx]
    print(idx)
    while next_three_idx <= 3 and idx + next_three_idx < len(joltage_adapters):
        total_connections += solve_num_connections(idx + next_three_idx, joltage)
        next_three_idx += 1
    return total_connections

res = solve_num_connections(0, 0)
print(res)