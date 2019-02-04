from Test import TestGate, unittest, import_module

class TestAnd16(TestGate.TestGate):
    def setUp(self):
        self.gate = 'And16'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
