# inside modulename.py
from myhdl import always_seq, block
@block
def Inc(count, enable, clock, reset):
    @always_seq(clock.posedge, reset=reset)  # sensitivity list
    def seq():
        if enable:
            count.next = count+1
    return seq

tests = [
    # count, enable
    [0, 0],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [2, 0],
    [3, 1],
]

results = []

# test bench for Inc
# from http://docs.myhdl.org/en/stable/manual/rtl.html
from myhdl import block, always, instance, Signal, ResetSignal, modbv, delay, StopSimulation, bin
ACTIVE_LOW, INACTIVE_HIGH = 0, 1
@block
def testbench():
    m = 3
    count = Signal(modbv(0)[m:])
    enable = Signal(bool(0))
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=0, async=True)
    inc = Inc(count, enable, clock, reset)
    HALF_PERIOD = delay(10)

    @always(HALF_PERIOD)
    def clockGen():
        clock.next = not clock

    @instance
    def stimulus():
        reset.next = ACTIVE_LOW
        yield clock.negedge
        reset.next = INACTIVE_HIGH

        for i in range(len(tests)):
            enable.next = tests[i][1]
            yield clock.negedge

        raise StopSimulation()

    @instance
    def monitor():
        print('count enable')
        yield reset.posedge
        while 1:
            yield clock.posedge
            yield delay(10)
            results.append(int(count)) # copy value of count, not reference to count
            print("   {}   {}".format(count, int(enable)))

    return clockGen, stimulus, monitor, inc


tb = testbench()
tb.run_sim()

test_counts = [x[0] for x in tests]
print(test_counts)
print(results)
print("tests {}= result ".format("!="[results == test_counts]))
