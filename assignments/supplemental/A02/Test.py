import unittest
from inspect import signature
from importlib import import_module
from myhdl import Signal, delay, Simulation

class TestGate:  # empty class prevents unittest running base class
    class TestGate(unittest.TestCase):
        def test_enough_tests(self):
            """Should supply 5 tests for each gate."""
            num_tests = len(self.m.tests)
            self.assertGreaterEqual(num_tests, 5)

        def test_correct_gate_name(self):
            """Gate name should match filename, except for '.py' at the end."""
            self.assertTrue(self.gate in self.m.__dict__)

        def test_correct_num_args(self):
            """Tests should have N elements for gate with N parameters."""
            arg_lengths = list(set([len(x) for x in self.m.tests]))
            self.assertEqual(len(arg_lengths), 1, 'some test is the wrong length')
            self.assertEqual(arg_lengths[0], len(signature(self.m.__dict__[self.gate]).parameters))

        # TODO the rest of the methods
        def test_simulation_works(self):
            """MyHDL simulation output should match given test values."""
            pass
