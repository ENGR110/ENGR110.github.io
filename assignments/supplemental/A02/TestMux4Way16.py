from Test import TestGate, unittest, import_module

class TestMux4Way16(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Mux4Way16'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
