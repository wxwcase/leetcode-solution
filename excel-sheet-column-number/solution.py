"""
Given a column title as appear in an Excel sheet, return its
corresponding column number

For example:
    A  -> 1
    B  -> 2
    C  -> 3
    ...
    Z  -> 26
    AA -> 27
    AB -> 28
    ...
"""
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if len(s) == 0:
            reversed = s[::-1]
            num, count = 0, 0
            for c in reversed:
                num += (ord(c) - ord('A') + 1) * (26 ** count)
                count += 1
        return num
