class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        else:
            s = self.countAndSay(n - 1) 
            return self._produceNextFromLast(s)

    def _produceNextFromLast(self, s):
        last = s[0]
        count = 1
        result = []
        if len(s) > 1:
            for c in s[1:]:
                if c == last:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(last)
                    last = c
                    count = 1
        else:
            result.append(str(count))
            result.append(last)
        return ''.join(result)

