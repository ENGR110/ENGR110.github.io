from myhdl import block, always_comb, Signal

from Not import Not
from And import And
from Or import Or

@block
def Xor(a, b, z):
    nota = Signal(0)
    notb = Signal(0)
    andanotb = Signal(0)
    andbnota = Signal(0)
    out = Signal(0)

    n1 = Not(a,nota)
    n2 = Not(b,notb)
    n3 = And(a,notb,andanotb)
    n4 = And(b,nota,andbnota)
    n5 = Or(andanotb,andbnota,out)
    
    @always_comb
    def f():
        z.next = out

    return f, n1, n2, n3, n4, n5
