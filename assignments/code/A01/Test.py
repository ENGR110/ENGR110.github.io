from myhdl import block, instance, delay, Signal

# two-input gate test harness
@block
def test_two(func):
    a, b, z = [Signal(0) for _ in range(3)]
    fun1 = func(a, b, z)

    @instance
    def tester():
        print("a b z")
        for i in [0, 1]:
            for j in [0, 1]:
                a.next, b.next = i, j
                yield delay(1)
                print(a, b, int(z))

    return fun1, tester


# one-input gate test harness
@block
def test_one(func):
    a, z = [Signal(0) for _ in range(2)]
    fun1 = func(a, z)

    @instance
    def tester():
        print("a z")
        for i in [0, 1]:
            a.next = i
            yield delay(1)
            print(a, int(z))

    return fun1, tester
