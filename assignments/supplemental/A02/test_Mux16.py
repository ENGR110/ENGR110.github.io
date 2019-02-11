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
def test_three_multibit(func,a,b,s,z,A,B,S):
    global OUTPUT
    fun1 = func(s, a, b, z)

    @instance
    def tester():
        #print("a\t\t\t b\t\t\t z") # optional
        for i in range(len(A)):
            a_str = A[i]
            b_str = B[i]
            s_str = S[i]

            if type(a) == list: 
                for j in range(len(a_str)):
                    a[j].next = int(a_str[j]) 
            else:
                a.next = int(a_str)
                 
            if type(b) == list:
                for j in range(len(b_str)): 
                    b[j].next = int(b_str[j])
            else:
                b.next = int(b_str)
            
            if type(s) == list:
                for j in range(len(s_str)): 
                    s[j].next = int(s_str[j])
            else: 
                s.next = int(s_str)
            
            yield delay(1)
            
            if type(z) == list:
                z_str = signals2bit_str(z)
            else:
                z_str = str(int(z))
                
            OUTPUT.append(z_str)
            #print(a_str,'\t',b_str,'\t',z_str)

    return fun1, tester

def copy_over(from_vec,to_vec):
    if type(from_vec) == list and type(to_vec) == list:
        for i in range(len(from_vec)):
            to_vec[i] = int(from_vec[i])
    else:
        to_vec = int(from_vec)

'''
Chip name: Mux16
Inputs: a[16], b[16], sel
Outputs: out[16]
Function: If sel=0 then for i=0..15 out[i]=a[i]
    else for i=0..15 out[i]=b[i].
'''
@block
def Mux16(select, inp_a, inp_b, out): # copy and paste
    @always_comb
    def foo():
        if int(select) == 0: copy_over(inp_a,out)
        else: copy_over(inp_b,out)
            
    return foo

def run_test(F,a,b,s,z,A,B,S):
    global OUTPUT
    test = test_three_multibit(F,a,b,s,z,A,B,S)
    test.run_sim()
    test_output = copy.deepcopy(OUTPUT) # keep a copy
    OUTPUT = [] # reset
    return test_output

# example: test 16-bit Or

a, b, s, z = get_Nbit_signal(16), get_Nbit_signal(16), Signal(0), get_Nbit_signal(16)
A, B, S = [], [], []

# randomly generate some test strings
for i in range(5):
    A.append(get_random_Nbit_str(16))
    B.append(get_random_Nbit_str(16))
    S.append(get_random_Nbit_str(1))

# test
test_output = run_test(Mux16,a,b,s,z,A,B,S)

# solution
soln_output = []
for i in range(5):
    a = bit_str2num(A[i])
    b = bit_str2num(B[i])
    s = bit_str2num(S[i])
    z = (s == 0)*a + (s == 1)*b
    soln_output.append(num2Nbit_str(z,16))

# compare results
for i in range(len(A)):
    if test_output[i] == soln_output[i]:
        print(test_output[i], soln_output[i],'ok')
    else:
        print(test_output[i], soln_output[i],'NOPE')
    
