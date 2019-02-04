from myhdl import block, always_comb, Signal

from Not import Not
from Or import Or

@block
def Ifxtheny(a, b, z):
    notx = Signal(0)
    out = Signal(0)

    n1 = Not(a, notx)
    n2 = Or(notx,b,out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2
