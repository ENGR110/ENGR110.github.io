from myhdl import always_comb, block, Signal

from Test import test_two
from Not import Not
from And import And

@block
def Notxandy(a, b, z):
    notx = Signal(0)
    out = Signal(0)

    n1 = Not(a, notx)
    n2 = And(notx, b, out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2


if __name__ == "__main__":
    test = test_two(Notxandy)
    test.run_sim()
