from myhdl import block, always_comb, Signal

from And import And

@block
def X(a, b, z):
    out = Signal(0)

    n1 = And(a, 1, out)

    @always_comb
    def f():
        z.next = out

    return f, n1
