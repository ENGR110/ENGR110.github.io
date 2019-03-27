from ac import *
# three styles of tests.

# style 1: straightforward, but a little tedious
test1 = encode('@5')
if test1 == '0000000000000101':
    print('test1 passed')
else:
    print('test1 failed')

test2 = encode('@12')
if test2 == '0000000000001100':
    print('test2 passed')
else:
    print('test2 failed')

test3 = encode('@2')
if test3 == '0000000000000010':
    print('test3 passed')
else:
    print('test3 failed')

# style 2, using lists of input and output:
ins = ['@5', '@12', '@32767', '@4']
outs = [
    '0000000000000101',
    '0000000000001100',
    '0111111111111111',
    '0000000000000100',
]

for i in range(len(ins)):
    try:
        if encode(ins[i]) == outs[i]:
            print('test' + str(i) + ': passed')
        else:
            print('test' + str(i) + ': failed')
    except:
        print('test' + str(i) + ':! had some sort of error')

cin = ['0;JMP', '0 ; JMP', 'D=A;JLE']
cout = ['1110101010000111',
        '1110101010000111',
        '1110110000010110']
for i in range(len(cin)):
    print('testing ' + str(i))
    try:
        if encode(cin[i]) == cout[i]:
            print('passed')
        else:
            print('failed')
    except:
        print('something something ...error')

# style 3: using a function
def tester(testname, a, b):
    try:
        passfail = 'pass' if encode(a) == b else 'fail'
        print(testname + ': ' + passfail)
    except:
        print(testname + ': had an error')

tester('test1', '@5',      '0000000000000101')
tester('test2', '@12',     '0000000000001100')
tester('test3', '@2',      '0000000000000010')
tester('test4', '0;JMP',   '1110101010000111')
tester('test5', '0 ; JMP', '1110101010000111')
tester('test6', 'D=A;JLE', '1110110000010110')
