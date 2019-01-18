from myhdl import block, always_comb, Signal
from Nand import Nand
from Test import test_two

@block
def Not(a, z):
    out = Signal(0)
    n1 = Nand(a, 1, out)

    @always_comb
    def f():
        z.next = out

    return f, n1


if __name__ == "__main__":
    test = test_two(Not)
    test.run_sim()
