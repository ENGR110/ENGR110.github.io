import sys
import proc

symbol_table = {
    'SCREEN': 0x4000, 'KBD': 0x6000,
    'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4
}

filename = sys.argv[-1]
with open(filename) as ff:
    f = proc.only_instructions(ff)

    # pass 1: symbols
    instruction_counter = 0
    for line in f:
        if '(' in line:
            name = line[1:-1]
            if name not in symbol_table:
                symbol_table[name] = instruction_counter
        else:
            instruction_counter += 1

print(symbol_table)
