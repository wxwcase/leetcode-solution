#!/usr/bin/env python3

def main():
    # Given a non-negative number represented as an array of digits, plus one to the number.
    # The digits are stored such that the most significant digit is at the head of the list.
    s1 = []
    s2 = [0]
    s3 = [1]
    s4 = [0, 1]
    s5 = [1, 0]
    s6 = [1, 2, 3]
    s7 = [1, 9]
    
    sol = Solution()    
    print(sol.plusOne(s1))
    print(sol.plusOne(s2))
    print(sol.plusOne(s3))
    print(sol.plusOne(s4))
    print(sol.plusOne(s5))
    print(sol.plusOne(s6))                    
    print(sol.plusOne(s7))    
    
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if len(digits) < 1:
            return [0]
        if len(digits) == 1:
            return [int(x) for x in str(digits[0] + 1)]
        result = digits[0]
        for d in digits[1:]:
            result *= 10
            result += d
        result += 1
        return [int(x) for x in str(result)]                                                            

if __name__ == '__main__':
    main()
