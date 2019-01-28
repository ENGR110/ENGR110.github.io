# Unit test for Assignment A01:
# https://engr110.github.io/assignments/A01.html
# This script will be uploaded to the autograder, and the pass/fail
# should provide feedback to students, as well as earn points for
# passing tests, and deduct points for failing tests

# You can run this script locally in the same file as the rest of your
# A01 python files.  Run it with the command:
# python3 UnitTest.py

import unittest
import sys
from importlib import import_module
from myhdl import Simulation, Signal, delay
from math import log2

class A01(unittest.TestCase):
    def assertion(self, z, name, truthtable_entry):
        self.assertEqual(int(z), truthtable_entry,
                         '{} output {} did not match expected {}'
                         .format(name, z, truthtable_entry))

    def test_single_input_gate(self):
        """Output should match truth table for single-input gates (Not)."""
        def test1(name, signals, truthtable):
            for i in [0, 1]:
                t_idx = int('{}'.format(i), 2)
                signals[0].next = i
                yield delay(1)
                self.assertion(signals[1], name, truthtable[t_idx])

        GATES = [['Not', [1,0]]]
        self.runner(test1, GATES)

    def test_two_input_gate(self):
        """Output should match truth table for 2-input gates."""
        def test2(name, signals, truthtable):
            for i in [0, 1]:
                for j in [0, 1]:
                    t_idx = int('{}{}'.format(i, j), 2)
                    signals[0].next, signals[1].next = i, j
                    yield delay(1)
                    self.assertion(signals[2], name, truthtable[t_idx])

        GATES = [
            ['Constant0',   [0,0,0,0]],
            ['And',         [0,0,0,1]],
            ['Xandnoty',    [0,0,1,0]],
            ['X',           [0,0,1,1]],
            ['Notxandy',    [0,1,0,0]],
            ['Y',           [0,1,0,1]],
            ['Xor',         [0,1,1,0]],
            # ['Or',          [0,1,1,1]],  # provided
            ['Nor',         [1,0,0,0]],
            ['Equivalence', [1,0,0,1]],
            ['Noty',        [1,0,1,0]],
            ['Ifythenx',    [1,0,1,1]],
            ['Notx',        [1,1,0,0]],
            ['Ifxtheny',    [1,1,0,1]],
            # ['Nand',        [1,1,1,0]],  # provided
            ['Constant1',   [1,1,1,1]],
        ]
        self.runner(test2, GATES)


    def runner(self, test, gates):
        """Run the tests."""
        num_signals = 1 + int(log2(len(gates[0][1])))  # n inputs, plus 1 output
        for gate in gates:
            with self.subTest(gate=gate):
                m = import_module(gate[0])
                f = m.__dict__[gate[0]]  # Module name must be the same as Gate name
                sigs = [Signal(0) for _ in range(num_signals)]
                check = test(gate[0], sigs, gate[1])
                sim = Simulation(f(*sigs), check)
                sim.run(quiet=1)
                print('OK: {}'.format(gate[0]))

if __name__ == "__main__":
    unittest.main(verbosity=0)
