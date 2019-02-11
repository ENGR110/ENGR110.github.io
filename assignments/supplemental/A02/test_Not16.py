import sys
import random # for randint
import copy # for deepcopy
from functools import reduce 

# for path issues in virtual environments
sys.path.append('/usr/local/lib/python3.6/dist-packages')
try: # test for failure
    import myhdl
except:
    print('failed to import myhdl, bailing')
    sys.exit(1)

# no explosions? carry on as usual
from myhdl import block, always_comb, Signal, intbv, delay, instances, instance

# get vector of Signals of length N
def get_Nbit_signal(N):
    if N <= 0:
        return []
        
    return [Signal(0) for _ in range(N)]

# get a random N-bit binary string
def get_random_Nbit_str(N):
    if N > 64 or N < 1 or type(N) != int:
        return ''

    S = format(random.randint(0,2**N-1), '#0'+str(N+2)+'b') # 16 bits + '0b'
    return S[2:]

# convert a vector of Signals to a bit string
def signals2bit_str(G):
    B = ''
    for i in range(len(G)):
        B += str(int(G[i]))
    return B

# convert a bit string to a base-10 number
def bit_str2num(q):
    return int(q,2)
    
# convert a base-10 number to an N-bit binary string
def num2Nbit_str(q,N):
    if N > 64 or N < 1 or type(N) != int:
        return ''

    S = format(q, '#0'+str(N+42)+'b') # N bits + junk
    return S[-N:]   

# cheap way of capturing output
OUTPUT = []

# two-input (m,n)-bit gate test harness with tests A and B
@block
def test_one_multibit(func,a,z,A):
    global OUTPUT
    fun1 = func(a, z)

    @instance
    def tester():
        #print("a\t\t\t b\t\t\t z") # optional
        for i in range(len(A)):
            a_str = A[i]
            for j in range(len(a_str)): a[j].next = int(a_str[j]) 
                
            yield delay(1)
            z_str = signals2bit_str(z)
            OUTPUT.append(z_str)
            #print(a_str,'\t',b_str,'\t',z_str)

    return fun1, tester

@block
def Not16(inp_a, out):
    @always_comb
    def foo():
        for i in range(16):
            out[i] = (int(inp_a[i]) + 1) % 2
            
    return foo

def run_test(F,a,z,A):
    global OUTPUT
    test = test_one_multibit(F,a,z,A)
    test.run_sim()
    test_output = copy.deepcopy(OUTPUT) # keep a copy
    OUTPUT = [] # reset
    return test_output

# simply inverting the bits and converting to an int fails in Python.
# Python interpets the leading bit as a sign bit with the remainder
# not as a two's complement integer. 
def flip_bit_char(s):
    return '1'*(s == '0') + '0'*(s == '1')

def invert_bit_str(S):
    S0 = [flip_bit_char(S[i]) for i in range(len(S))]
    return reduce(lambda x,y: x + y,S0)

# example: test 16-bit Or

a, z = get_Nbit_signal(16), get_Nbit_signal(16)
A = []

# randomly generate some test strings
for i in range(5):
    A.append(get_random_Nbit_str(16))

# test
test_output = run_test(Not16,a,z,A)

# solution
soln_output = []
for i in range(5):
    a = A[i]
    s = invert_bit_str(a)
    soln_output.append(s)

# compare results
for i in range(len(A)):
    if test_output[i] == soln_output[i]:
        print(A[i],test_output[i], soln_output[i],'ok')
    else:
        print(A[i], test_output[i], soln_output[i],'NOPE')
    
