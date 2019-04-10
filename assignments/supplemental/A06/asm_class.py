class assembler:
    def __init__(x):
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
                self.lines.append(line.strip())

    def get_labels(self):
        icount = 0
        for line in self.lines:
            if self.is_instruction(line):
                icount += 1
            if line[0] == '(':
                self.st[line[1:-1]] = icount

    def get_vars(self):
        vcount = 16
        for line in self.lines:
            if line[1:] not in self.st:
                if line[0] == '@':
                    self.st[line[1:]] = vcount
                    vcount += 1

    def is_instruction(self, line):
        return line[0] != '/' and line[0] != '('

if __name__ == "__main__":
    filename = 'tests/vars.asm'
    a = assembler()
    a.read_asm(filename)
    # for line in a.lines:
    #     print(a.is_instruction(line))
    a.get_labels()
    a.get_vars()
    print(a.st)
