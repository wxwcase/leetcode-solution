#!/usr/bin/env python3

def main():
    pass

class Solution:
    """Given an array of integers, every element appears twice except for one. Find that single one.

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    """
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for item in A:
            result ^= item 
        return result

if __name__ == '__main__':
    main()