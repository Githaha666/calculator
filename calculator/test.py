import unittest
from calculator.parser import parser
from decimal import Decimal
from calculator.eval_exceptions import EvalException, SyntaxException, TokensException
class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = parser

    def test_number(self):
        self.assertEqual(self.parser.parse('123'), 123)
        self.assertEqual(self.parser.parse('123.456'), Decimal('123.456'))
        self.assertEqual(self.parser.parse('-123.456'), Decimal('-123.456'))
        self.assertEqual(self.parser.parse('+-123.456'), Decimal('-123.456'))
    
    def test_binop(self):
        self.assertEqual(self.parser.parse('1 + 2'), 3)
        self.assertEqual(self.parser.parse('1 - 2'), -1)
        self.assertEqual(self.parser.parse('1 * 2'), 2)
        self.assertEqual(self.parser.parse('1 / 2'), Decimal('0.5'))
        self.assertEqual(self.parser.parse('1 % 2'), 1)
        self.assertEqual(self.parser.parse('1 ^ 2'), 1)
        self.assertEqual(self.parser.parse('1 + 2 * 3'), 7)
        self.assertEqual(self.parser.parse('1 + 2 * 3 / 4'), Decimal('2.5'))
        self.assertEqual(self.parser.parse('50^2 * pi * 2'), Decimal('15707.963268')) # Cylinder test V = r^2 * pi * h

    
    def test_unary(self):
        self.assertEqual(self.parser.parse('-1'), -1)
        self.assertEqual(self.parser.parse('+1'), 1)
        self.assertEqual(self.parser.parse('-(1 + 2)'), -3)
        self.assertEqual(self.parser.parse('+(1 + 2)'), 3)
        self.assertEqual(self.parser.parse('-(1 + 2) * 3'), -9)
        self.assertEqual(self.parser.parse('+(1 + 2) * 3'), 9)
        self.assertEqual(self.parser.parse('+(-(1 + 2)) * 3 / 4'), Decimal('-2.25'))
    
    def test_error(self):
        self.assertRaises(TokensException, self.parser.parse, '1 a')
        self.assertRaises(SyntaxException, self.parser.parse, '1 +')
        self.assertRaises(EvalException, self.parser.parse, '1 / 0')
        self.assertRaises(EvalException, self.parser.parse, 'root(-1)')
    
    def test_root(self):
        self.assertEqual(self.parser.parse('root(4)'), 2)
        self.assertEqual(self.parser.parse('4root(16)'), 2)
        self.assertEqual(self.parser.parse('2+2 root(16)'), 2)
        self.assertEqual(self.parser.parse('2+2 root(16) + 2'), 4)
        self.assertEqual(self.parser.parse('5 + (2+2 root(16)) + (2root(4))'), 9)
        self.assertEqual(self.parser.parse('4 + (root(16)) + 4'), 12)
    
    def test_constants(self):
        self.assertEqual(self.parser.parse('pi'), Decimal('3.1415926536'))
        self.assertEqual(self.parser.parse('e'),  Decimal('2.7182818285'))
        self.assertEqual(self.parser.parse('tau'),Decimal('6.2831853072'))

# Execute tests

def tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    tests()