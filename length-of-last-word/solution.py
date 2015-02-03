class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s[::-1].strip()
        count = 0
        for c in s:
            if not c.isalpha():
                return count
            else:
                count += 1
        return count
