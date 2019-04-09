# assignment 6.1
import sys

# return True if x contains an A instruction, False otherwise
def is_a_instruction(x):
    return True # replace with your code

# return the translated A instruction
def translate(x):
    return '1111000011110000'  # replace with your code

filename = sys.argv[-1]
with open(filename) as f:
    for line in f:
        if is_a_instruction(line):
            print(translate(line))

