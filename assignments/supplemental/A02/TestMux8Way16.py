from Test import TestGate, unittest, import_module
from myhdl import delay, Signal, Simulation
import sys

class TestMux8Way16(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Mux8Way16'
        self.m = import_module(self.gate)

    def test_sim(self):
        """Simulate the gate, ensure logic works."""
        provided_tests = self.m.tests  # [[], [], [], [], []]
        def run_a_test(att):
            # all Signal(0)
            sigs = []
            for num in att[:-1]:
                sigs.append(Signal(0))
            output = Signal(0)

            n1 = self.m.__dict__[self.gate](*sigs, output)
            for i,x in enumerate(att[:-1]):
                sigs[i].next = x
                yield delay(1)
            return output
            
        for atest in provided_tests:
            output = run_a_test(atest)
            self.assertEqual(int(output), atest[-1])  # want to ensure that out == atest[-1]

            sim = Simulation(self.m.__dict__[self.gate](*sigs), n1)
            sim.run(quiet=0)

if __name__ == '__main__':
    unittest.main()
