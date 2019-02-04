from myhdl import block, always_comb, Signal, intbv, delay, instances, instance
from Nand import Nand
from Not import Not
from Test import test_two

@block
def And(a, b, z):
    nandab = Signal(0)
    out = Signal(0)

    n1 = Nand(a, b,nandab)
    n2 = Not(nandab, out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2


if __name__ == "__main__":
    test = test_two(And)
    test.run_sim()
