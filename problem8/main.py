def solve_part_one(raw_instructions):
    instruction_idx = 0
    accumulator = 0
    read_instructions = set()
    while instruction_idx < len(raw_instructions):
        instruction = raw_instructions[instruction_idx]
        if instruction_idx in read_instructions:
            print("We've already read this instruction")
            print(instruction_idx)
            print(accumulator)
            break
        read_instructions.add(instruction_idx)

        pieces = instruction.split()
        command = pieces[0]
        unit = int(pieces[1])
        print(instruction_idx)

        if command == "nop" or command == "acc":
            instruction_idx += 1

            if command == "acc":
                accumulator += unit
        elif command == "jmp":
            instruction_idx += unit
        else:
            raise Exception(f"Command '{command}' invalid'")

    print(f"Final Accumulator: {accumulator}")

def solve_part_two(raw_instructions):
    """
    Strategy:
    - Iterate through instructions once
        - find list of "success instructions" - instructions
        after the loop begins that enable you to get to the end
        - save list of indicies of all nop and jmp instructions
    - Iterate through list of saved jmp/nop instructions
        - see if modifying any of them enable you to reach one of the "success instructions"
    - After finding the cursed instruction, modify raw and rerun to find accumulator
    """

    # Step one - iterate and build success and jmp/np list
    potential_corrupted_instructions = set()
    success_instructions = set()
    visited_instructions = set()
    instruction_idx = 0
    accumulator = 0
    execution_order = []
    while instruction_idx < len(raw_instructions):
        visited_instructions.add(instruction_idx)
        execution_order.append(instruction_idx)
        command_pieces = raw_instructions[instruction_idx].split()
        if command_pieces[0] in set(["jmp","nop"]):
            potential_corrupted_instructions.add(instruction_idx)

        if instruction_idx in success_instructions:
            # We've reached a loop. Failure.
            print(instruction_idx)
            print("We've reached a loop! Reset")
            while(instruction_idx in visited_instructions):
                instruction_idx += 1
            print(success_instructions)
            success_instructions = set()

            continue

        success_instructions.add(instruction_idx)

        # Continue execution as normal.
        command = command_pieces[0]
        unit = int(command_pieces[1])
        if command == "nop" or command == "acc":
            instruction_idx += 1

            if command == "acc":
                accumulator += unit
        elif command == "jmp":
            instruction_idx += unit
        else:
            raise Exception(f"Command '{command}' invalid'")


    print("We have a list of winning instructions")
    print(success_instructions)
    print("We also have a list of potentially corrupted instructions")
    print(potential_corrupted_instructions)


    print("Now - attempting to modify the jmps/nops and seeing if they get me to the end")
    commands_to_modify = set([])
    for corrupt_command_idx in potential_corrupted_instructions:
            command_pieces = raw_instructions[corrupt_command_idx].split()
            command = command_pieces[0]
            unit = int(command_pieces[1])
            if command == "nop" and corrupt_command_idx + unit in success_instructions:
                print("DING DING WE HAVE A WINNER")
                print(raw_instructions[corrupt_command_idx])
                print(corrupt_command_idx)
                commands_to_modify.add(corrupt_command_idx)
            elif command == "jmp" and corrupt_command_idx + 1 in success_instructions:
                print("DING DING WE HAVE A WINNER")
                print(raw_instructions[corrupt_command_idx])
                print(corrupt_command_idx)
                commands_to_modify.add(corrupt_command_idx)
    print(commands_to_modify)

    command_to_modify = None
    for command in execution_order:
        if command in commands_to_modify:
            print("We have found the chosen one!")
            print(command)
            command_to_modify = command
            break

    # Let's modify the corrupt command
    command_pieces = raw_instructions[command_to_modify].split()
    command = command_pieces[0]
    unit = int(command_pieces[1])
    if command == "nop":
        command = "jmp"
    elif command == "jmp":
        command = "nop"
    else:
        raise Exception(f"This makes no sense: {command}")
    raw_instructions[command_to_modify] = f"{command} {unit}"


    # Now run the first part.
    solve_part_one(raw_instructions)


with open('problem8/input.txt', 'r') as file:
    raw_instructions = file.read().splitlines()

print(raw_instructions)
solve_part_one(raw_instructions)
solve_part_two(raw_instructions)
