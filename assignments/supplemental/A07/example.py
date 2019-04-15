from myhdl import *


@block
def a_register(mux16_out,c0,addressM):
    # inputs: mux16_out
    # input: c0 is ~instruction[15]
    # output: something

    # overboard for assignment 7, but awesome:
    # notc0 = Signal(bool())
    # n1 = Not(c0, notc0)
    # r1 = Register(mux16, notc0, something)
    # @always_seq()
    # def f():

@block
def program_counter(addressM,reset,c,pc):
    # inputs: something, reset
    # input: c is result of truth table
    # output: pc
    pass


@block
def CPU(addressM, ...):
