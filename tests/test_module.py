import unittest
from src.module_logic import run

class TestModuleLogic(unittest.TestCase):
    def test_run(self):
        self.assertIsNone(run())

if __name__ == '__main__':
    unittest.main()
