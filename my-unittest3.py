import unittest
from calc import Calc

class TestCale(unittest.TestCase):
    def setUp(self):
       self.calc3 = Calc()

       
    def test_multiplicacion(self):
        self.assertEqual(4, self.calc.multiplicacion(2,2))
        self.assertEqual(12, self.calc.multiplicacion(1,12))
        self.assertEqual(500, self.calc.multiplicacion(10,50))
        self.assertEqual(0, self.calc.multiplicacion(0,0))
        self.assertEqual("Invalid", self.calc.multiplicacion(1,-1))


        if __name__ == '__main__':
         unittest.main()
