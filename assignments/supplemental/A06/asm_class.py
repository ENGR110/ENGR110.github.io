class assembler(object):
    def __init__(x, name):
        x.name = name
        x.lines = []
        x.st = {
            'SCREEN': 0x4000,
            'KBD': 0x2000,
            'SP': 0,
            'R0': 0, 'R1': 1, 'R2': 2
        }

    def read_asm(self, filename):
        with open(filename) as f:
            for line in f:
                self.lines.append(line)

    def get_labels(self):
        icount = 0
        for line in self.lines:
            if self.is_instruction(line):
                icount += 1
            if self.is_label(line):
                self.st[self.only_label(line)] = icount

    def get_vars(self):
        vcount = 16
        for line in self.lines:
            if line[1:-1] not in self.st:
                if line[0] == '@':
                    self.st[line[1:-1]] = vcount
                    vcount += 1

    def is_instruction(self, line):
        if line.isspace():
            return False
        for c in line:
            if c.isspace() and c != '/' and c != '(':
                return True
            if c == '/' or c == '(':
                return False
        # return None

    def only_label(self, line):
        # given "     (label)    ", return "label"
        # "    (LOOP)   "
        return line[1:-2]

    def is_label(self, line):
        # TODO watch out for commented-out lines
        #  //    this is (a comment)
        return '(' in line

# st: {
# (should still have SCREEN, etc.)
# 'i':         16,
# 'counter':   17,
# 'hello':     18,
# 'this_has:special$characters':   19
# }

if __name__ == "__main__":
    filename = 'tests/vars.asm'
    a = assembler('a')
    a.read_asm(filename)
    # for line in a.lines:
    #     print(a.is_instruction(line))
    a.get_labels()
    a.get_vars()
    print(a.st)
