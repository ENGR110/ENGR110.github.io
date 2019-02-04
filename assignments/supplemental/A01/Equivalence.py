from myhdl import block, always_comb, Signal

from Not import Not
from And import And
from Or import Or

@block
def Equivalence(a, b, z):
    notx = Signal(0)
    noty = Signal(0)
    andxy = Signal(0)
    andnotxnoty = Signal(0)
    out = Signal(0)

    n1 = Not(a, notx)
    n2 = Not(b, noty)
    n3 = And(a,b,andxy)
    n4 = And(notx,noty,andnotxnoty)
    n5 = Or(andxy,andnotxnoty,out)

    @always_comb
    def f():
        z.next = out

    return f, n1, n2, n3, n4, n5
