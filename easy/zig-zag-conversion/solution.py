#!/usr/bin/env python3

def main():
    test()

def test():
    s1 = 'PAYPALISHIRING'
    r1 = 'PAHNAPLSIIGYIR'
    n1 = 3

    s2 = 'ABCDEFGHIJKLMN'
    r2 = 'AGMBFHLNCEIKDJ'
    n2 = 4

    sol = Solution()
    print(r1, sol.convert(s1, n1))
    print(r2, sol.convert(s2, n2))

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s == '' or nRows == 0:
            return ''
        matrix = [[] for i in range(nRows)]
        down = True 
        count = 0
        stringPtr = 0
        matrix[count].append(s[stringPtr])
        while stringPtr < len(s):
            while down and stringPtr < len(s):
                count += 1
                count %= nRows
                stringPtr += 1                                   
                if stringPtr < len(s):                    
                    matrix[count].append(s[stringPtr])
                if count == (nRows - 1) or count == 0:
                    down = not down 
            while not down and stringPtr < len(s):
                count -= 1
                count %= nRows
                stringPtr += 1                    
                if stringPtr < len(s):
                    matrix[count].append(s[stringPtr])
                if count == (nRows - 1) or count == 0:
                    down = not down

        result = [x for sub in matrix for x in sub]
        result = ''.join(result)
        return result

if __name__ == '__main__':
    main()