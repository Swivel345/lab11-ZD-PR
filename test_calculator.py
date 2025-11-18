import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 100) == 0

    def test_divide(self): # 3 assertions
        assert divide(2, 10) == 5
        assert divide(5, 20) == 4
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(math.hypot(3, 4), 5)
        self.assertEqual(math.hypot(5, 12), 13)
        self.assertEqual(math.hypot(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            sqrt(-9)

        self.assertEqual(sqrt(25), 5)
        self.assertEqual(sqrt(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()