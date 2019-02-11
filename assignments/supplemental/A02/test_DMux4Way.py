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
from myhdl import block, always_comb, Signal, intbv, delay, instances, instance, always

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

    S = format(random.randint(0,2**N-1), '#0'+str(N+42)+'b') # 16 bits + '0b'
    return S[-N:]

# convert a vector of Signals to a bit string
def signals2bit_str(G):
    B = ''
    for i in range(len(G)):
        B += str(int(G[i].next))
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
def test_three_multibit(func,s,n,a,b,c,d,S,N,A,B,C,D):
    global OUTPUT
    fun1 = func(s, n, a, b, c, d)

    @instance
    def tester():
        #print("a\t\t\t b\t\t\t z") # optional
        for i in range(len(S)):
            s_str = S[i]
            n_str = N[i]
            a_str = A[i]
            b_str = B[i]
            c_str = C[i]
            d_str = D[i]

            # performing the selector bits assignment first does not fix the timing problem
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

            if type(c) == list:
                c_str = signals2bit_str(c)
            else:
                c_str = str(int(c))

            if type(d) == list:
                d_str = signals2bit_str(d)
            else:
                d_str = str(int(d))
                
            OUTPUT.append((a_str,b_str,c_str,d_str))

    return fun1, tester

def copy_over(from_vec,to_vec):
    if type(from_vec) == list and type(to_vec) == list:
        for i in range(len(from_vec)):
            to_vec[i].next = int(from_vec[i].next)
    else:
        to_vec.next = int(from_vec.next)

@block
def DMux8Way(select, inp, out_a, out_b, out_c, out_d): # copy and paste
    @always_comb
    def foo():
        selection = bit_str2num(signals2bit_str(select))   
        if selection == 0: 
            copy_over(inp,out_a)
            copy_over(ZERO,out_b)
            copy_over(ZERO,out_c)
            copy_over(ZERO,out_d)
        elif selection == 1: 
            copy_over(ZERO,out_a)
            copy_over(inp,out_b)
            copy_over(ZERO,out_c)
            copy_over(ZERO,out_d)
        elif selection == 2: 
            copy_over(ZERO,out_a)
            copy_over(ZERO,out_b)
            copy_over(inp,out_c)
            copy_over(ZERO,out_d)
        elif selection == 3: 
            copy_over(ZERO,out_a)
            copy_over(ZERO,out_b)
            copy_over(ZERO,out_c)
            copy_over(inp,out_d)  
            
    return foo

def run_test(func,s,n,a,b,c,d,S,N,A,B,C,D):
    global OUTPUT
    test = test_three_multibit(func,s,n,a,b,c,d,S,N,A,B,C,D)
    test.run_sim()
    test_output = copy.deepcopy(OUTPUT) # keep a copy
    OUTPUT = [] # reset
    return test_output

# example: test 16-bit Or

s, n = get_Nbit_signal(2), Signal(0)
a, b, c, d = Signal(0), Signal(0), Signal(0), Signal(0)
S, N, A, B, C, D, = [], [], [], [], [], []

# randomly generate some test strings
for i in range(5):
    S.append(get_random_Nbit_str(2))
    N.append(get_random_Nbit_str(1))
    A.append('0')
    B.append('0')
    C.append('0') 
    D.append('0')

# test
test_output = run_test(DMux8Way,s,n,a,b,c,d,S,N,A,B,C,D)

# solution
soln_output = []
for i in range(5):
    s = bit_str2num(S[i])
    n = bit_str2num(N[i])
    a = (s == 0)*n
    b = (s == 1)*n
    c = (s == 2)*n
    d = (s == 3)*n
    soln_output.append((num2Nbit_str(a,1),num2Nbit_str(b,1),num2Nbit_str(c,1),num2Nbit_str(d,1)))

# compare results
for i in range(len(A)):
    s = bit_str2num(S[i])
    n = bit_str2num(N[i])    
    a = A[i]
    b = B[i]
    c = C[i]
    d = D[i]   
    
    if test_output[i] == soln_output[i]:
        print(s,n,a,b,c,d,'-',test_output[i],soln_output[i],'ok')
    else:
        print(s,n,a,b,c,d,'-',test_output[i],soln_output[i],'NOPE')
    
