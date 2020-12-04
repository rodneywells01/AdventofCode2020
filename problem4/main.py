data = None
formatted_entries = []


required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

with open('problem4/input.txt', 'r') as file:
    data = file.readlines()

    entry = ""
    for row in data:
        if row == "\n":
            # Entry finalized.

            # Sanitize and convert to dict
            sanitized_entry = entry.replace("\n", "").split()
            formatted_entry = {}
            for field in sanitized_entry:
                key_val_pair = field.split(":")
                formatted_entry[key_val_pair[0]] = key_val_pair[1]

            # Store for later
            formatted_entries.append(formatted_entry)

            # Reset entry
            entry = ""
        else:
            entry += f" {row}"


    print(formatted_entries)
    # for entry in formatted_entries:
    #     print(entry.split())


def solve_part_one():
    required_fields_set = set(required_fields)
    valid_passports = 0
    for entry in formatted_entries:
        if not len(required_fields_set - entry.keys()):
            valid_passports += 1


    print(valid_passports)

def solve_part_two():
    # Omit entries with missing fields.
    required_fields_set = set(required_fields)
    valid_passports = []
    for entry in formatted_entries:
        if not len(required_fields_set - entry.keys()):
            valid_passports.append(entry)

    # Validate passports
    true_valid_passports = []
    for passport in valid_passports:
        height_key = passport["hgt"][len(passport["hgt"])-2:]
        height_value = passport["hgt"][:len(passport["hgt"])-2:]

        valid = validate_min_max(passport["byr"], VALIDATION_RULES["byr"]) \
            and validate_min_max(passport["iyr"], VALIDATION_RULES["iyr"]) \
            and validate_min_max(passport["eyr"], VALIDATION_RULES["eyr"]) \
            and height_key in VALIDATION_RULES["hgt"] \
            and validate_min_max(height_value, VALIDATION_RULES["hgt"][height_key]) \
            and validate_ecl(passport["ecl"]) \
            and validate_hex(passport["hcl"]) \
            and validate_pid(passport["pid"]) \
            and height_key in VALIDATION_RULES["hgt"] \


        if valid:
            true_valid_passports.append(passport)

    print(true_valid_passports)
    print(len(true_valid_passports))

def validate_pid(pid):
    if len(pid) != 9:
        return False
    try:
        int(pid)
    except ValueError:
        return False

    return True

def validate_ecl(color):
    return color in VALIDATION_RULES["ecl"]["valid_values"]

def validate_hex(value):
    if value[0] != "#":
        return False
    value = value[1:]
    if len(value) != 6:
        return False

    try:
        int(value, 16)
    except ValueError:
        return False

    return True

def validate_min_max(value, validation_rule):
    try:
        value = int(value)
    except ValueError:
        return False

    return value >= validation_rule["min"] and value <= validation_rule["max"]

VALIDATION_RULES = {
    "byr": {
        "min": 1920,
        "max": 2002
    },
    "iyr": {
        "min": 2010,
        "max": 2020
    },
    "eyr": {
        "min": 2020,
        "max": 2030
    },
    "hgt": {
        "cm": {
            "min": 150,
            "max": 193
        },
        "in": {
            "min": 59,
            "max": 76
        }
    },
    "ecl": {
        "valid_values": [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]
    }
}



solve_part_one()
solve_part_two()
