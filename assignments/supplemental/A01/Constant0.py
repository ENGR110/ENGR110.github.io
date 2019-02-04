from myhdl import block, always_comb, Signal

@block
def Constant0(a, b, z):
    out = Signal(0)

    @always_comb
    def f():
        z.next = out

    return f
