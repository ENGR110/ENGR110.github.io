from Test import TestGate, unittest, import_module
from myhdl import block, Signal, delay, instance, bin, intbv
import random
class TestOr16(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Or16'
        self.m = import_module(self.gate)

    def signals2str(self, G):
        B = ''
        for i in range(len(G)):
            B += str(int(G[i]))
        return B

    def test_simulation_works_with_given_values(self):
        """MyHDL simulation output should work with 'tests' values."""
        GIVEN_TABLE = self.m.__dict__['tests']

        def b16(x):
            return bin(x, width=16)

        # two-input 16-bit gate test harness
        @block
        def test_two_16bit(func):
            a, b, z = [[Signal(0) for _ in range(16)] for _ in range(3)]
            fun1 = func(a, b, z)

            @instance
            def tester():
                print('')
                print("a\t\t\t b\t\t\t z\t\t\t OK?")
                for testcase in GIVEN_TABLE:
                    a_int, b_int = map(intbv, testcase[:2])
                    a_str, b_str = map(b16, [a_int, b_int])
                    for j in range(16):
                        a[15-j].next, b[15-j].next = a_int[j], b_int[j]
                        yield delay(1)
                    sigs = list(map(lambda x: int(self.signals2str(x),2), [a,b,z]))
                    self.assertEqual(sigs[-1], testcase[-1])
                    self.assertEqual(sigs[0] | sigs[1], sigs[2])
                    self.assertEqual(sigs[0] | sigs[1], testcase[-1] )

                    OK = sigs[0]|sigs[1] == testcase[2]
                    print('{}\t{}\t{}\t{}'.format(*map(b16, sigs), OK*'yes'+(not OK)*'no'))

            return fun1, tester

        Or16 = self.m.__dict__[self.gate]  # basically "from foo import foo" where foo is passed in as a string

        test = test_two_16bit(Or16)
        test.run_sim(quiet=1)


    def test_simulation_works_with_random_values(self):
        """MyHDL simulation output should work if given random values."""

        def get_random_16bit_str():
            S = format(random.randint(0,2**16-1), '#018b') # 16 bits + '0b'
            return S[2:]

        # two-input 16-bit gate test harness
        @block
        def test_two_16bit(func):
            a, b, z = [[Signal(0) for _ in range(16)] for _ in range(3)]
            fun1 = func(a, b, z)

            @instance
            def tester():
                print('')
                print("a\t\t\t b\t\t\t z\t\t\t OK?")
                for i in range(5):
                    a_str = get_random_16bit_str()
                    b_str = get_random_16bit_str()
                    for j in range(16):
                        a[j].next, b[j].next = int(a_str[j]), int(b_str[j])
                    yield delay(1)
                    z_str = self.signals2str(z)
                    OK = (int(a_str,2) | int(b_str,2) == int(z_str,2))
                    print(a_str,'\t',b_str,'\t',z_str,'\t',OK*'yes'+(not OK)*'no')

            return fun1, tester

        Or16 = self.m.__dict__[self.gate]  # basically "from foo import foo" where foo is passed in as a string

        test = test_two_16bit(Or16)
        test.run_sim(quiet=1)

if __name__ == '__main__':
    unittest.main()
