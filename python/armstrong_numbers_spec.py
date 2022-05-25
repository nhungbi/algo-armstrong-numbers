# The code is written as driver code. Can you convert it to Unit Test?
from armstrong_numbers import find_armstrong_numbers
import unittest

class TestArmstrong(unittest.TestCase):

    def test_armstrong(self):
        self.assertEqual(find_armstrong_numbers([0]), [0])
        self.assertEqual(find_armstrong_numbers(list(range(0, 8))), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(find_armstrong_numbers(list(range(0, 100))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(find_armstrong_numbers(list(range(0, 999))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])


if __name__ == '__main__':
    unittest.main()


# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
