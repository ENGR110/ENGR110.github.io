# fibonacci
import subprocess

# get a line from a file
def newlineless(ls):
    while ls.endswith('\n'):
        ls = ls[:-1]
    return ls

for i in ['\n', 'hi\n\n', 'asdfj', '\n\n\n', 'hello\nworld\n']:
    print(newlineless(i))

def read_asm(name):
    # @15
    # D=A
    # 0;JMP
    ls = []
    with open(name) as f:
        for line in f:
            ls.append(newlineless(line))
    return ls

prog = read_asm('test.hack')
# proc = subprocess.run(['wc -l test.hack'], stdout=True, shell=True)
if len(prog) == 4:
    print("passed")
else:
    print("failed")
