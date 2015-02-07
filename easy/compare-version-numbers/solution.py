#!/usr/bin/env python3

def main():
    test()

def test():
    sol = Solution()
    version1 = '0.0'
    version2 = '0.1'
    version3 = '0.0.1'
    version4 = '0.1'
    version5 = '0.0.2'
    version6 = '1.0.1'
    version7 = '1.2'
    print('-1', sol.compareVersion(version1, version2))
    print('-1', sol.compareVersion(version1, version3))
    print('-1', sol.compareVersion(version1, version4))
    print('-1', sol.compareVersion(version1, version5))
    print('-1', sol.compareVersion(version1, version6))
    print('-1', sol.compareVersion(version1, version7))
    print('1', sol.compareVersion(version2, version3))
    print('0', sol.compareVersion(version2, version4))
    print('1', sol.compareVersion(version2, version5))
    print('-1', sol.compareVersion(version2, version6))
    print('-1', sol.compareVersion(version2, version7))
    print('-1', sol.compareVersion(version3, version4))
    print('-1', sol.compareVersion(version3, version5))
    print('-1', sol.compareVersion(version3, version6))
    print('-1', sol.compareVersion(version3, version7))
    print('1', sol.compareVersion(version4, version5))
    print('-1', sol.compareVersion(version4, version6))
    print('-1', sol.compareVersion(version4, version7))
    print('-1', sol.compareVersion(version5, version6))
    print('-1', sol.compareVersion(version5, version7))    
    print('-1', sol.compareVersion(version6, version7))
    print('0', sol.compareVersion(version2, version2))

class Solution:
    """If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0"""
    # @param version1, a string
    # @param version2, a string
    # @param an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        delta = abs(len(v1) - len(v2))
        max = len(v1) if len(v1) > len(v2) else len(v2)
        if len(v1) < len(v2):
            v1.extend([0] * delta)
        else:
            v2.extend([0] * delta)
        for i in range(max):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0

if __name__ == '__main__':
    main()