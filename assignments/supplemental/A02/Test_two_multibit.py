import sys
import random
import copy

# insert profanity-laced rant here
sys.path.append('/usr/local/lib/python3.6/dist-packages')
try:
    import myhdl
except:
    print('failed to import myhdl, bailing')
    sys.exit(1)

from myhdl import block, always_comb, Signal, intbv, delay, instances, instance

def get_Nbit_signal(N):
    if N <= 0:
        return []
        
    return [Signal(0) for _ in range(N)]

def get_random_Nbit_str(N):
    if N > 64 or N < 1 or type(N) != int:
        return ''

    S = format(random.randint(0,2**N-1), '#0'+str(N)+'b') # 16 bits + '0b'
    return S[2:]

def signals2str(G):
    B = ''
    for i in range(len(G)):
        B += str(int(G[i]))
    return B

OUTPUT = []

# two-input 16-bit gate test harness
@block
def test_two_multibit(func,a,b,z,A,B):
    global OUTPUT
    fun1 = func(a, b, z)

    @instance
    def tester():
        print("a\t\t\t b\t\t\t z")
        for i in range(len(A)):
            a_str = A[i]
            b_str = B[i]

            for j in range(len(a_str)): a[j].next = int(a_str[j]) 
            for j in range(len(b_str)): b[j].next = int(b_str[j])
                
            yield delay(1)
            z_str = signals2str(z)
            OUTPUT.append(z_str)
            #print(a_str,'\t',b_str,'\t',z_str)

    return fun1, tester

@block
def Or16(inp_a, inp_b, out):
    @always_comb
    def foo():
        for i in range(16):
            out[i] = inp_a[i] | inp_b[i]
            
    return foo

@block
def soln_Or16(inp_a, inp_b, out):
    @always_comb
    def foo():
        for i in range(16):
            out[i] = inp_a[i] | inp_b[i]
            
    return foo

a, b, z = get_Nbit_signal(16), get_Nbit_signal(16), get_Nbit_signal(16)
A, B = [], []

for i in range(5):
    A.append(get_random_Nbit_str(16))
    B.append(get_random_Nbit_str(16))

test = test_two_multibit(Or16,a,b,z,A,B)
test.run_sim()
test_output = copy.deepcopy(OUTPUT)
OUTPUT = []

test = test_two_multibit(soln_Or16,a,b,z,A,B)
test.run_sim()
soln_output = copy.deepcopy(OUTPUT)

for i in range(len(OUTPUT)):
    print(test_output[i], soln_output[i])
    if test_output[i] == soln_output[i]:
        print('ok')
