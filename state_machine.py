import collections

# Define terminal colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

# Print machine state transition
def print_tape_transition(pos, state, transition, tape, blank):
    pos_copy = pos
    tape_copy = tape.copy()

    if (pos_copy < 0):
        tape_copy.insert(0, bcolors.BOLD + bcolors.UNDERLINE + bcolors.WARNING + blank + bcolors.ENDC)
        pos_copy = 0
    elif pos_copy + 1 > len(tape):
        tape_copy.append(bcolors.BOLD + bcolors.UNDERLINE + bcolors.WARNING + blank + bcolors.ENDC)
        pos_copy = 0
    else:
        tape_copy[pos_copy] = bcolors.BOLD + bcolors.UNDERLINE + bcolors.WARNING + tape_copy[pos_copy] + bcolors.ENDC

    print(f"[{''.join(tape_copy)}] ({state}, {tape_copy[pos_copy]})", end='')
    print(f" -> ({transition['to_state']}, {transition['write']}, {transition['action']})")

def read_tape(pos, tape, machine):
    if (pos < 0 or pos + 1 > len(tape)):
        return machine['blank']
    else:
        return tape[pos]

def write_tape(pos, write, tape):
    if (pos < 0):
        tape.insert(0, write)
        pos = 0
    elif pos + 1 > len(tape):
        tape.append(write)
    else:
        tape[pos] = write

def run_state_machine(machine_input, machine_description):
    tape = collections.deque(list(machine_input))
    pos = 0
    machine = machine_description
    steps = 0

    tape.append(machine['blank'])

    state = machine['initial']

    print('Running machine description: ' + machine['name'])

    while state not in machine['finals']:
        transition = False
        # Finding the correct transition for the state and current tape value 
        for item in machine['transitions'][state]:
            if str(item['read']) != read_tape(pos, tape, machine):
                continue
            else:
                transition = item
                break

        # Check if condition exists
        if transition == False:
            raise LookupError(f"No transition found for {read_tape(pos, tape, machine)} in {state}")

        print_tape_transition(pos, state, transition, tape, machine['blank'])

        write_tape(pos, transition['write'], tape)
        state = transition['to_state']

        steps += 1
        if transition['action'] == 'RIGHT':
            pos += 1
        elif transition['action'] == 'LEFT':
            pos -= 1
        else:
            raise ValueError(f"Transition action '{transition['action']}' is not supported.")

    tape.pop()
    print('\n -- Resulting tape: ' + ''.join(tape) + ' - Steps: ' + str(steps))