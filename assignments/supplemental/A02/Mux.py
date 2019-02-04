from myhdl import block, always_comb

@block
def Mux(select, inp_a, inp_b, out):

    @always_comb
    def f():
        out.next = inp_b if select else inp_a

    return f

tests = [
  [0, 0, 0, 0],
  [1, 1, 1, 1],
  [0, 1, 0, 1],
  [1, 0, 0, 1],
  [1, 0, 1, 1],
]
