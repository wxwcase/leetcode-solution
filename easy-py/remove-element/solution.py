#!/usr/bin/env python3

def main():
    test1()

def test1():
    sol = Solution()
    a1 = [];           e1 = 0
    a2 = [4, 5];       e2 = 4
    a3 = [1, 4, 4, 5]; e3 = 4
    a4 = [1]         ; e4 = 1
    r1 = sol.removeElement(a1, e1)
    r2 = sol.removeElement(a2, e2)
    r3 = sol.removeElement(a3, e3)    
    r4 = sol.removeElement(a4, e4)
    print(r1)    
    print(r2)
    print(r3)
    print(r4)

class Solution:
    """Given an array and a value, remove all instances of that value in place, and return the new length. 
    
       The order of elements can be changed. 
       It doesn't matter what you leave beyond the new length.
    """
    def removeElement(self, A, elem):
        if not elem in A:
            return len(A)
        while elem in A:
            A.remove(elem)
        return len(A)
        result = list(filter(lambda x: x != elem, A))
        return len(result)

if __name__ == '__main__':
    main()