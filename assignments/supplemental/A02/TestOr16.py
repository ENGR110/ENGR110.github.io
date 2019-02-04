from Test import TestGate, unittest, import_module

class TestOr16(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Or16'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
