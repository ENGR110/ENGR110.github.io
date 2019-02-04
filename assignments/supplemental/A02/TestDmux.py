from Test import TestGate, unittest, import_module

class TestDmux(TestGate.TestGate):
    def setUp(self):
        self.gate = 'Dmux'
        self.m = import_module(self.gate)

if __name__ == '__main__':
    unittest.main()
