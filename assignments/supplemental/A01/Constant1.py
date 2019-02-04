from myhdl import block, always_comb, Signal
from Test import test_two

@block
def Constant1(a, b, z):
    out = Signal(1)

    @always_comb
    def f():
        z.next = out

    return f

if __name__ == "__main__":
    t = test_two(Constant1)
    t.run_sim()
