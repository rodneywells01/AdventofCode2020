
class Bag:
    def __init__(self, color, contains):
        self.color = color
        self.contained_bags = contains

class BagRule:
    def __init__(self, color, qty):
        self.color = color
        self.qty = qty

def generate_bag_info(raw_rules):
    storage_rules = {}
    RULE_LEN = 3
    for rule in raw_rules:
        # Process a rule.
        rule_list = rule.split()
        color = " ".join(rule_list[:2]) # Color is the first 2 words
        rest = rule_list[2:]
        contained_bags = {}
        idx = 4 # Remaining rulesets begin at the 4th index

        while idx + RULE_LEN <= len(rule_list):
            # Iterate through the rest of the rule, adding in containing bags
            new_rule = rule_list[idx: idx+RULE_LEN]
            if " ".join(new_rule) == "no other bags.":
                # This bag contains no other bags
                break

            qty = int(new_rule[0])
            rule_color = " ".join(new_rule[1:3])

            # Store the contained bag rule with the color and quantity.
            contained_bags[rule_color] = {
                "qty": qty
            }
            idx += RULE_LEN + 1


        # Generate the bag entry
        storage_rules[color] = Bag(
            color=color,
            contains=contained_bags
        )

    return storage_rules


def does_contain_color(bag, target_color):
    if bag.color in memoized_gold_containing:
        return memoized_gold_containing[bag.color]
    elif target_color in bag.contained_bags:
        # Success! Bag was found.
        memoized_gold_containing[bag.color] = True
        return True
    else:
        # Check all of the contained bags.
        print(bag.contained_bags)
        results = any([does_contain_color(bag_info[sub_bag], target_color) for sub_bag in bag.contained_bags])
        if results:
            # Success! Bag was found.
            memoized_gold_containing[bag.color] = True
            return True
        # Bag does not exist.
        memoized_gold_containing[bag.color] = False
        return False

# Process all of the rules into a useable datastructure.
raw_rules = None
with open('problem7/input.txt', 'r') as file:
    raw_rules = file.read().splitlines()
bag_info = generate_bag_info(raw_rules)
memoized_gold_containing = {}



def solve_part_one():
    """
    Calculate how many different bag colors contain gold.
    """
    bags_with_gold = []
    TARGET_COLOR = "shiny gold"
    for bag_color in bag_info:
        if does_contain_color(bag_info[bag_color], TARGET_COLOR):
            bags_with_gold.append(bag_color)

    print(f"{len(bags_with_gold)} bags can hold gold")


def get_bag_quantity(bag):
    """
    Given a bag, count how many bags are within this bag. Includes itself.
    """
    return 1 + sum([bag.contained_bags[sub_bag]["qty"] * get_bag_quantity(bag_info[sub_bag]) \
        for sub_bag in bag.contained_bags])

def solve_part_two():
    """
    Calculate the total bags in a shiny gold bag.
    """
    shiny_gold_bag = bag_info["shiny gold"]

    # We want the total bags IN a shiny gold bag - so subtract itself.
    total_bags = get_bag_quantity(shiny_gold_bag) - 1

    print(f"Total bags in 1 gold bag: {total_bags}")


solve_part_one()
solve_part_two()
