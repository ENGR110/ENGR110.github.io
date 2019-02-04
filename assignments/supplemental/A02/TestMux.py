from Test import TestGate, unittest, import_module

class TestMux(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Mux'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
