import sys
import random # for randint
import copy # for deepcopy

# for path issues in virtual environments
sys.path.append('/usr/local/lib/python3.6/dist-packages')
try: # test for failure
    import myhdl
except:
    print('failed to import myhdl, bailing')
    sys.exit(1)

# no explosions? carry on as usual
from myhdl import block, always_comb, Signal, intbv, delay, instances, instance

ZERO = Signal(0)

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

    S = format(q, '#0'+str(N+2)+'b') # 16 bits + '0b'
    return S[2:]   

# cheap way of capturing output
OUTPUT = []

# two-input (m,n)-bit gate test harness with tests A and B
@block
def test_three_multibit(func,s,n,a,b,S,N,A,B):
    global OUTPUT
    fun1 = func(s, n, a, b)

    @instance
    def tester():
        for i in range(len(S)):
            s_str = S[i]
            n_str = N[i]
            a_str = A[i]
            b_str = B[i]

            if type(s) == list:
                for j in range(len(s_str)): 
                    s[j].next = int(s_str[j])
            else: 
                s.next = int(s_str)

            if type(n) == list: 
                for j in range(len(n_str)):
                    n[j].next = int(n_str[j]) 
            else:
                n.next = int(n_str)
                 
            yield delay(1)
            
            if type(a) == list:
                a_str = signals2bit_str(a)
            else:
                a_str = str(int(a))

            if type(b) == list:
                b_str = signals2bit_str(b)
            else:
                b_str = str(int(b))
                
            OUTPUT.append((a_str,b_str))

    return fun1, tester

def copy_over(from_vec,to_vec):
    if type(from_vec) == list and type(to_vec) == list:
        for i in range(len(from_vec)):
            to_vec[i] = int(from_vec[i])
    else:
        to_vec.next = int(from_vec)

@block
def DMux(select, inp, out_a, out_b): # copy and paste
    @always_comb
    def foo():
        if int(select) == 0: 
            copy_over(inp,out_a)
            copy_over(ZERO,out_b)
        else: 
            copy_over(ZERO,out_a)
            copy_over(inp,out_b)
            
    return foo

def run_test(F,s,n,a,b,S,N,A,B):
    global OUTPUT
    test = test_three_multibit(F,s,n,a,b,S,N,A,B)
    test.run_sim()
    test_output = copy.deepcopy(OUTPUT) # keep a copy
    OUTPUT = [] # reset
    return test_output

# example: test 16-bit Or

s, n, a, b = Signal(0), Signal(0), Signal(0), Signal(0)
S, N, A, B = [], [], [], []

# randomly generate some test strings
for i in range(5):
    S.append(get_random_Nbit_str(1))
    N.append(get_random_Nbit_str(1))
    A.append('0')
    B.append('0')    

# test
test_output = run_test(DMux,s,n,a,b,S,N,A,B)

# solution
soln_output = []
for i in range(5):
    s = bit_str2num(S[i])
    n = bit_str2num(N[i])    
    a = (s == 0)*n 
    b = (s == 1)*n
    soln_output.append((num2Nbit_str(a,1),num2Nbit_str(b,1)))

# compare results
for i in range(len(A)):
    s = bit_str2num(S[i])
    n = bit_str2num(N[i])
    a = bit_str2num(A[i])
    b = bit_str2num(B[i])

    if test_output[i] == soln_output[i]:
        print(s,n,test_output[i], soln_output[i],'ok')
    else:
        print(s,n,test_output[i], soln_output[i],'NOPE')
    
