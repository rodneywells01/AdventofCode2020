WINDOW_LENGTH = 25

# Read input
with open('problem9/input.txt', 'r') as file:
    xmas_code = file.read().splitlines()

preamble = xmas_code[:WINDOW_LENGTH]
idx = WINDOW_LENGTH
invalid_value = None
while idx < len(xmas_code):
    value = int(xmas_code[idx])

    # Find matching two values in preamble.
    preamble = set(xmas_code[idx - WINDOW_LENGTH: idx])
    valid = False
    for potential_match in preamble:
        if str(value - int(potential_match)) in preamble:
            valid = True
            break
    if not valid:
        print(f"No matching sum for {value}")
        invalid_value = value
        break

    print(value)
    print(preamble)
    idx += 1



left_idx = 0
right_idx = 0
while right_idx < len(xmas_code):
    summed_value = sum(int(value) for value in xmas_code[left_idx: right_idx])
    if summed_value < invalid_value:
        right_idx += 1
    elif summed_value > invalid_value:
        left_idx += 1
    else:
        print("Gottem")
        weakness_range = xmas_code[left_idx: right_idx]
        print(weakness_range)
        minval = min(weakness_range)
        maxval = max(weakness_range)
        print(minval)
        print(maxval)
        print(int(minval) + int(maxval))
        break
