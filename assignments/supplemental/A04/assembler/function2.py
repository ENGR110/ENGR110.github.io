# fibonacci

# get a line from a file
def read_asm(name):
    # @15
    # D=A
    # 0;JMP
    ls = [0, 0, 0]
    # ls = []
    # ls.append(2) # [2]
    # ls.append(42) # [2, 42]
    i = 0
    with open(name) as f:
        for line in f:
            ls[i] = line
            while ls[i][-1] == '\n':
                ls[i] = ls[i][0:-1]
            i += 1
    return ls

prog = read_asm('test.hack')

if prog == ['@15', 'D=A', '0;JMP']:
    print("passed")
else:
    print("failed")
