#!/usr/bin/env python3

def main():
    sol = Solution()
    a1 = [1, 1, 2];          r1 = 1
    a2 = [2, 2];             r2 = 2
    a3 = [3, 3, 4, 5];       r3 = 3
    a4 = [1, 4, 4, 4, 5, 6]; r4 = 4
    a5 = [8, 8, 7, 7, 7];    r5 = 7
    print('expected: ', r1, 'actual: ', sol.majorityElement(a1))
    print('expected: ', r2, 'actual: ', sol.majorityElement(a2))
    print('expected: ', r3, 'actual: ', sol.majorityElement(a3))
    print('expected: ', r4, 'actual: ', sol.majorityElement(a4))
    print('expected: ', r5, 'actual: ', sol.majorityElement(a5))

class Solution:
    """Given an array of size n, find the majority element. 
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.
    """
    def majorityElement(self, num):
        # @param num, a list of integers
        # @return an integer
        result = []
        number = len(num) // 2
        tmpMap = {}
        for n in num:
            if n in tmpMap:
                count = tmpMap[n]
                count += 1
                tmpMap[n] = count
            else:
                tmpMap[n] = 1
        for key in tmpMap:
            if tmpMap[key] >= number:
                result.append((key, tmpMap[key]))
        (max, maxcount) = result[0]
        for (i, j) in result:
            if j > maxcount:
                max = i 
        return max

if __name__ == '__main__':
    main()