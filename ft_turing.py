import argparse
import json

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

# Basic logic for validating input using python standard library argparse
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('jsonfile', type=argparse.FileType('r'), help='json description of the machine')
parser.add_argument('input', help='input of the machine')

# Parsing arguments and loading json file
args = parser.parse_args()

machine = json.load(args.jsonfile)

# TODO: Add validation for the actual input

print('Running machine description: ' + machine['name'])

# initial machine state values
tape = list(args.input)
tape.extend(list(machine['blank'] * 1))
state = machine['initial']
pos = 0

# Function to print current state of tape
def print_tape():
    tape_print = tape.copy()
    tape_print[pos] = bcolors.BOLD + bcolors.UNDERLINE + bcolors.WARNING + tape_print[pos] + bcolors.ENDC
    print(f"[{''.join(tape_print)}] ({state}, {tape[pos]})", end='')

# Read the current pos of the tape
def read_tape_block():
    if len(tape) >= pos + 1:
        return str(tape[pos])
    else:
        return str(machine['blank'])

# State machine
while state not in machine['finals']:
    transition = False
    # Finding the correct transition for the state and current tape value 
    for item in machine['transitions'][state]:
        if str(item['read']) != read_tape_block():
            continue
        else:
            transition = item
            break

    # Check if condition exists
    if transition == False:
        raise LookupError(f"No transition found for {str(read_tape_block())} in {state}")

    print_tape()
    print(f" -> ({transition['to_state']}, {transition['write']}, {transition['action']})")
    state = transition['to_state']
    tape[pos] = transition['write']
    
    if transition['action'] == 'RIGHT':
        pos += 1
    elif transition['action'] == 'LEFT':
        pos -= 1
    else:
        raise ValueError(f"Transition action '{transition['action']}' is not supported.")

tape.pop()
print('\n -- Result: ' + ''.join(tape))