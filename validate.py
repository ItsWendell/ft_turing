def validate_machine_descriptor(machine_descriptor):
    machine_keys = ['name', 'alphabet', 'blank', 'states', 'initial', 'finals', 'transitions']

    # Basic two way key detection for machine description
    machine_keys_diff1 = [item for item in list(machine_keys) if not item in list(machine_descriptor.keys())]
    if len(machine_keys_diff1):
        print("The following item(s) are missing in the machine decription: " + str(machine_keys_diff1))
        return False
    
    machine_keys_diff2 = [item for item in list(machine_descriptor.keys()) if not item in list(machine_keys)]
    if len(machine_keys_diff2):
        print("The following item(s) don't belong in the machine decription: " + str(machine_keys_diff2))
        return False

    # Basic state validation
    # print(machine_descriptor['transitions'].keys())

    # TODO: Add empty tape state validation to input

    # TODO: Input chars outside of characters

    # TODO: Check transitions with state

    return True