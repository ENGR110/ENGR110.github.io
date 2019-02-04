from myhdl import block, always_comb, Signal

from Not import Not

@block
def Noty(a, b, z):
    out = Signal(0)

    n1 = Not(b, out)

    @always_comb
    def f():
        z.next = out

    return f, n1
