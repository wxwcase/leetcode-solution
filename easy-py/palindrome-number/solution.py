#!/usr/bin/env python3

import unittest

def main():
    pass 

class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.a1 = 11
        self.a2 = 1001
        self.a3 = 121
        self.a4 = 12321
        self.a5 = 12320
        self.a6 = 1000021
        self.a7 = 1000110001
        self.a8 = 2222222

    def tearDown(self):
        del self.sol 

    def testTrue(self):
        self.assertTrue(self.sol.isPalindrome(self.a1))
        self.assertTrue(self.sol.isPalindrome(self.a2))
        self.assertTrue(self.sol.isPalindrome(self.a3))
        self.assertTrue(self.sol.isPalindrome(self.a4))
        self.assertFalse(self.sol.isPalindrome(self.a5))
        self.assertFalse(self.sol.isPalindrome(self.a6))
        self.assertTrue(self.sol.isPalindrome(self.a7))                
        self.assertTrue(self.sol.isPalindrome(self.a8))        

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True 
        elif x // pow(10, len(str(x)) - 1) != x % 10:
            return False
        else:
            for i in range(2, len(str(x)) // 2 + 1):
                if (x // pow(10, len(str(x)) - i) % 10) != (x // pow(10, i - 1) % 10):
                    return False 
            return True

if __name__ == '__main__':
    unittest.main()