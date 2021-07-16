import unittest
from calc import Calc

class TestCale(unittest.TestCase):
    def setUp(self):
       self.calc4 = Calc()

    def test_division(self):
        self.assertEqual(1, self.calc.division(2,2))
        self.assertEqual(2, self.calc.division(24,12))
        self.assertEqual(8, self.calc.division(40,5))
        self.assertEqual(0, self.calc.division(0,0))
        self.assertEqual("Invalid", self.calc.division(1,-1))


        if __name__ == '__main__':
         unittest.main()