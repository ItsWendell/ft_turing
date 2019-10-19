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
machineInput = args.input

# TODO: Add validation for the actual input

print('Running machine description: ' + machine['name'])

# initial machine state values
tape = list(machineInput);
state = machine['initial']
pos = 0

# Function to print current state of tape
def print_tape():
    tape_print = tape.copy()
    tape_print[pos] = bcolors.UNDERLINE + tape_print[pos] + bcolors.ENDC
    print(f"[{''.join(tape_print)}] ({state}, {tape[pos]})", end='')

# State machine
while state not in machine['finals']:
    transition = False
    # Finding the correct transition for the state and current tape value 
    for item in machine['transitions'][state]:
        if str(item['read']) != str(tape[pos]):
            continue
        else:
            transition = item

    # Check if condition exists
    if transition == False:
        print(f"No transition found for {str(tape[pos])} in {state}")
        exit()

    print_tape()
    state = transition['to_state']
    tape[pos] = transition['write']
    print(f" -> ({state}, {tape[pos]}, {transition['action']})")
    if transition['action'] == 'RIGHT':
        pos += 1
    elif transition['action'] == 'LEFT':
        pos -= 1
    else:
        print('Something unexpected happened, this action does not exist')
        exit()

print('\n -- Result: ' + ''.join(tape))