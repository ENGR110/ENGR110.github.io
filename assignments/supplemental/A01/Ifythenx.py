from myhdl import block, always_comb, Signal

from Not import Not
from Or import Or

@block
def Ifythenx(a, b, z):
    noty = Signal(0)
    out = Signal(0)

    n1 = Not(b, noty)
    n2 = Or(noty,a,out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2
