class Solution:
    # @return a string
    def concertToTitle(self, num):
        if num < 27:
            return chr(num - 1 + ord('A'))
        mod = (num - 1) % 26 + 1
        num = (num - 1) // 26
        chars = []
        while num != 0:
            chars += [chr(mod - 1 + ord('A'))]
            mod = (num - 1) % 26 + 1
            num = (num - 1) // 26
        chars += [chr(mod - 1 + ord('A'))]
        chars = chars[::-1]
        return ''.join(chars)
