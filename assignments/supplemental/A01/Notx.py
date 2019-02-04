from myhdl import Signal, block, always_comb

from Not import Not

@block
def Notx(a, b, z):
    out = Signal(0)

    n1 = Not(a, out)

    @always_comb
    def f():
        z.next = out

    return f, n1
