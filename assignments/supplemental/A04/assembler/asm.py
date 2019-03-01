# two versions of the same idea.
# First, as two separate functions, which
# can be used independently:
def a_to_bin(s):
    if s[0] == '@':
        int_s = int(s[1:])
        if int_s >= 2**15:
            raise
        return bin(int_s)
    else:
        return s

def pad(bits):
    if bits[0:2] == '0b':
        b = bits[2:]
        return ('0'*(16-len(b)))+b
    else:
        return bits

# However, because these 2 functions are separate,
# it is a good idea to leave some documentation
# to give a clue about how to use it:
# s = pad(a_to_bin(x))


# Alternative approach, check '@' outside, then process
# the A-instruction completely within a single function
def assemble(line):
    if line[0] == '@':
        return ab(line)
    else:
        return line

def ab(s):
    int_s = int(s[1:])
    if int_s >= 2**15:
        raise
    int_b = bin(int_s)
    b = int_b[2:] # remove '0b'
    return ('0'*(16-len(b)))+b

