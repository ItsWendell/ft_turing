import argparse
import collections
import json
from state_machine import run_state_machine
from validate import validate_machine_descriptor

def main():
    # Basic logic for validating arguments using python standard library argparse
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('jsonfile', type=argparse.FileType('r'), help='json description of the machine')
    parser.add_argument('input', help='input of the machine')

    # Parsing arguments and loading json file
    args = parser.parse_args()
    machine = json.load(args.jsonfile)

    machine.keys()

    # TODO: Add validation for the actual input
    validate_machine_descriptor(machine)

    run_state_machine(args.input, machine)

if __name__ == "__main__":
    main()