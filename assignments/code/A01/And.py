from myhdl import block, always_comb, Signal, intbv, delay, instances, instance
from Nand import Nand
from Not import Not
from Test import test_two

@block
def And(a, b, z):
    out = Signal(intbv(0))
    out2 = Signal(intbv(0))

    n1 = Nand(a, b, out)
    n2 = Not(out, out2)

    @always_comb
    def f():
        z.next = out2

    return f, n1, n2


if __name__ == "__main__":
    test = test_two(And)
    test.run_sim()
