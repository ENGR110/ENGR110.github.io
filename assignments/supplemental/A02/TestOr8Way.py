from Test import TestGate, unittest, import_module

class TestOr8Way(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Or8Way'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
