from myhdl import block, always_comb, Signal
from Nand import Nand
from Not import Not
from Test import test_two

@block
def Or(a, b, z):
    nota = Signal(0)
    notb = Signal(0)
    out = Signal(0)

    n1 = Not(a, nota)
    n2 = Not(b, notb)
    n3 = Nand(nota, notb, out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2, n3


if __name__ == "__main__":
    test = test_two(Or)
    test.run_sim()
