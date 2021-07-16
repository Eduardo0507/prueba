import unittest
from calc import Calc

class TestCale(unittest.TestCase):
    
    def setUp(self):
       self.calc2 = Calc()

    def test_resta(self):
        self.assertEqual(3, self.calc.resta(6,3))
        self.assertEqual(13, self.calc.resta(26,13))
        self.assertEqual(500, self.calc.resta(750,250))
        self.assertEqual(0, self.calc.resta(1,1))
        self.assertEqual("Invalid", self.calc.resta(1,-1))


        if __name__ == '__main__':
         unittest.main()
