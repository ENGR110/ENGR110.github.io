from Test import TestGate, unittest, import_module

class TestDMux8Way(TestGate.TestGate):
    def setUp(self):
        self.gate = 'DMux8Way'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
