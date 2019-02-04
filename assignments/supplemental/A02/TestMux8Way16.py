from Test import TestGate, unittest, import_module

class TestMux8Way16(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Mux8Way16'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
