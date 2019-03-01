# ac.py
# given an A or C instruction in Hack assembly language,
# output the corresponding Hack machine code for that instruction.

# first step: split the whole instruction into 3 parts
def split(s):
    # default values for dest, comp and jump:
    comp = s  # the input string
    dest = ''  # (dest is optional)
    jump = ''  # (comp is optional)

    # if there is an '=' take all the text to its left as 'dest'
    if "=" in s:
        dest = s.split("=")[0]
        comp = s.split("=")[1]  # take everything to the right as 'comp'

    # if there is a ';' take all the text to its right as 'jump'
    if ";" in s:
        jump = s.split(";")[1]
        # comp = s.split(";")[0]   # SUBTLE BUG! s might still have an '=' sign...
        comp = comp.split(";")[0]  # ...but this works

    return [dest, comp, jump]


# next step: look up the bits which match the given instruction
def lookup_jump(jump):
    # Suggested implementation: use a dictionary of "key":"value" pairs
    jt = {
        # NOTE: attempting to fetch a key that doesn"t exist is a KeyError in Python
        "":    "000",  # null
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111",
    }
    return jt[jump] # jt["JGE"] should return "011"

# TODO - use a similar look-up table approach for dest and comp
def lookup_comp(comp):
    pass

def lookup_dest(dest):
    pass

def encode_a(inst):
    # example: encode_a("@234") returns '0000000011101010'
    ii = int(inst[1:])
    if ii < 0 or ii >= 2**15:
        raise
    b = bin(ii)[2:]  # remove the '0b' from the start
    return '0' * (16-len(b)) + b

def encode_c(inst):
    # C instruction format:
    # "dest=comp;jump"
    #       ^^^^         (required)
    # examples:
    # "M=D+A"
    # "D-1;JGE"
    # "M=D+1;JMP"
    dest, comp, jump = split(inst)
    ldest = lookup_dest(dest)
    lcomp = lookup_comp(comp)
    ljump = lookup_jump(jump)
    return '111' + ldest + lcomp + ljump

def encode_ac(line):
    # Given an A or C instruction, encode it as Hack machine code.
    # Return a string of 16 1s or 0s.
    if line[0] == '@':
        encode_a(line[1:]) # TODO - handle symbols
    else:
        encode_c(line)
