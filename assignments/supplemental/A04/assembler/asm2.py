# two implementations of translating an A-instruction
# in each implementation, A-instructions are translated
# from the '@234' format into the 16-bit form with a leading 0,
# unless the input is not an A-instruction, in which case
# we simply return the input without modifying it.

# The first approach splits the work of translating the
# A-instruction into two phases:

# First function: split the '@' symbol off and convert the number portion
# into a string of '1' and '0' characters using the bin function
def ainst(s):
    if s[0] == '@':
        return bin(int(s[1:]))
    else:
        return s

# Second function: remove the '0b' and pad with leading zeros
# to make the whole string 16 bits long.
def pad0(s):
    if s[0:2] == '0b':
        return (('0'*16)+s[2:])[-16:]
    else:
        return s

# instructions for how to use these 2 functions together:
# pad0(ainst('@42'))


# The second approach tests for an '@' symbol in one function,
# then does the entire job of converting to '1' and '0' characters in a single function.
# This is less multi-functional than the earlier appraoch, but possibly easier to use.

# First, test for the presence of the '@' symbol
# then call a single function a2 which does the whole job of convering.
# Otherwise (if no '@' symbol) return the original string s.
def assemble(s):
    if s[0] == '@':
        return a2(s)
    else:
        return s

def a2(s):
    a = int(s[1:])
    # generate an error if the input is outside of the range from [0..2**15)
    if (a < 0) or (a >= 2**15):
        raise
    return (('0'*16)+a[2:])[-16:]


