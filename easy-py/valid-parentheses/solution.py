class Solution:
    # @return a boolean
    def isValide(self, s):
        lefty  = '{[('
        righty = '}])'
        stack = []
        for c in s:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if len(stack) == 0:
                    return False
                elif lefty[righty.find(c)] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
