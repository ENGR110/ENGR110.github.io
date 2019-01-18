from myhdl import block, always_comb, Signal, intbv, instance, delay
from Test import test_two

@block
def Nand(a, b, out):
    @always_comb
    def f():
        out.next = not (a and b)
    return f

if __name__ == "__main__":
    test = test_two(Nand)
    test.run_sim()
