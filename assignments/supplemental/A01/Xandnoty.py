from myhdl import block, always_comb, Signal

from Test import test_two
from Not import Not
from And import And

@block
def Xandnoty(a, b, z):
    noty = Signal(0)
    out = Signal(0)

    n1 = Not(b, noty)
    n2 = And(a, noty, out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2

if __name__ == "__main__":
    t = test_two(Xandnoty)
    t.run_sim()
