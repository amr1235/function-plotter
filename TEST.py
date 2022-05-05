import unittest
from lib.interface import isFunction

class isFunctionTest(unittest.TestCase) :
    def test_case_1(self) :
        self.assertEqual(isFunction("(x^2)"),True,"TEST CASE 1")
    def test_case_2(self) :
        self.assertEqual(isFunction("x^2)"),False,"TEST CASE 2")
    def test_case_3(self) :
        self.assertEqual(isFunction("(x2)"),False,"TEST CASE 3")
    def test_case_4(self) :
        self.assertEqual(isFunction("(x^2) * "),False,"TEST CASE 4")
    def test_case_5(self) :
        self.assertEqual(isFunction("(x^2) * (2x)"),False,"TEST CASE 5")
    def test_case_6(self) :
        self.assertEqual(isFunction("(x^2) * (2*x)"),True,"TEST CASE 6")
    def test_case_7(self) :
        self.assertEqual(isFunction("(x^2)     * 2"),True,"TEST CASE 7")
    def test_case_8(self) :
        self.assertEqual(isFunction("(x^2) + 2 * (x**2)"),False,"TEST CASE 8")
    def test_case_9(self) :
        self.assertEqual(isFunction("x"),True,"TEST CASE 9")
    def test_case_10(self) :
        self.assertEqual(isFunction("-"),False,"TEST CASE 10")
    def test_case_11(self) :
        self.assertEqual(isFunction(""),False,"TEST CASE 11")
    def test_case_12(self) :
        self.assertEqual(isFunction("-x"),False,"TEST CASE 12")
    def test_case_13(self) :
        self.assertEqual(isFunction("-1"),True,"TEST CASE 13")
    def test_case_14(self) :
        self.assertEqual(isFunction("X"),True,"TEST CASE 14")
    def test_case_15(self) :
        self.assertEqual(isFunction("2*x + X"),True,"TEST CASE 15")
    def test_case_16(self) :
        self.assertEqual(isFunction("X + (2*x)"),True,"TEST CASE 16")
    def test_case_17(self) :
        self.assertEqual(isFunction("-1 * x"),True,"TEST CASE 17")
    def test_case_18(self) :
        self.assertEqual(isFunction("x ^ -1"),True,"TEST CASE 18")
    def test_case_19(self) :
        self.assertEqual(isFunction("(x ^ -2) * -1 - 5"),True,"TEST CASE 19")
    def test_case_20(self) :
        self.assertEqual(isFunction("-2 * x^2"),True,"TEST CASE 20")

if __name__ == '__main__':  
    unittest.main()  