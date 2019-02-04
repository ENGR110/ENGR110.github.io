from myhdl import block, always_comb, Signal

from Or import Or
from Not import Not

@block
def Nor(a, b, z):
    orab = Signal(0)
    out = Signal(0)

    n1 = Or(a, b, orab)
    n2 = Not(orab, out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2
