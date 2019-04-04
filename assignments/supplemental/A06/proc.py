# remove comments
# remove whitsepace

# symbols:
# recognize them
# map them to memory locations
symbols = []
def find_symbol(line):
    # anything after @ which is not a number
    # (sym) things inside parentheses
    sym = ''
    if line[0] == '@':
        if not line[1:].isnumeric():
            sym = line[1:] # validate sym (skipping this step for now)
    if line[0] == '(':
        sym = line[1:-1]  # remove '(' and ')', leaving the symbol
    return sym

def map_symbol():
    pass

def remove_whitespace(f):
    ls = []
    for line in f:
        this_line = ""
        for ch in line:
            if ch != '\n' and ch != ' ':
                this_line += ch
        if this_line != '':
            ls.append(this_line)
    return ls

def remove_comments(f):
    ls = []
    for line in f:
        this_line = ""
        for i in range(len(line)):
            # hack comment: // ... \n
            if line[i] == '/' and line[i+1] == '/':
                break
            this_line += line[i]
        if this_line != '':
            ls.append(this_line)
    return ls

if __name__ == "__main__":
    with open("a.hack") as f:
        # print(remove_whitespace(remove_comments(f)))
        commentless = remove_comments(f)
        spaceless = remove_whitespace(commentless)
        for line in spaceless:
            print(find_symbol(line))
