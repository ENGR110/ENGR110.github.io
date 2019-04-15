# remove comments
# remove whitsepace

# symbols:
# recognize them
# map them to memory locations
labels = []
label_num = []
def find_symbol(line, linenum):
    # anything after @ which is not a number
    # (sym) things inside parentheses
    sym = ''
    inc = 1
    if line[0] == '@':
        if not line[1:].isnumeric():
            sym = line[1:] # validate sym (skipping this step for now)
    if line[0] == '(':
        inc = 0
        sym = line[1:-1]  # remove '(' and ')', leaving the symbol
        labels.append(sym)
        label_num.append(linenum + 1)
    return [sym, inc]

def map_symbol(line):
    # assume already made one pass with find_symbol
    # replace @LOOP with @5 etc.
    if line[0] == '@':
        if not line[1:].isnumeric():
            this_label = line[1:] # validate sym (skipping this step for now)
            if this_label in labels:
                # replace @val with the number
                return '@' + str(label_num[labels.index(this_label)])
    return line

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

def only_instructions(f):
    return remove_whitespace(remove_comments(f))

if __name__ == "__main__":
    with open("a.hack") as f:
        # print(remove_whitespace(remove_comments(f)))
        commentless = remove_comments(f)
        spaceless = remove_whitespace(commentless)
        remove_comments(remove_whitespace(f))
        # remove_comments(f)  # returns ["line"]
        # remove_whitespace(f) # returns ["line"]
        i = 0
        for line in spaceless:
            [s, j] = find_symbol(line, i)
            i += j
        for line in spaceless:
            print(line, map_symbol(line))

        print(labels)
        print(label_num)
