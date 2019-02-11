# Increment with reset
# from http://docs.myhdl.org/en/stable/manual/rtl.html
from myhdl import always_seq, block

@block
def Inc(count, enable, clock, reset):
    # count: output
    # enable: control, increment when 1 else retain last value
    # clock: input
    # reset: asynchronous reset input
    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            count.next = count+1

    return seq
