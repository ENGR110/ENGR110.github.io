# import ac
from ac import *

# test it, verbose and tedious:
# test1 = ac.encode_ac('@5')
# print('test1')
# if test1 == '0000000000000101':
#     print('passed')
# else:
#     print('failed')

# test2 = ac.encode_ac('@12')
# print('test2')
# if test2 == '0000000000001100':
#     print('passed')
# else:
#     print('failed')

# test3 = ac.encode_ac('@2')
# print('test2')
# if test3 == '0000000000001100':
#     print('passed')
# else:
#     print('failed')

# test, short and loopy:
ins = ['@5', '@12', '@32768', '@4']
outs = [
    '0000000000000101',
    '0000000000001100',
    '0111111111111111',
    '0000000000000100',
]

for i in range(len(ins)):
    print('testing ' + str(i))
    try:
        if encode_ac(ins[i]) == outs[i]:
            print('passed')
        else:
            print('failed')
    except:
        print('something had an error')
