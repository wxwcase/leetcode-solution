#!/usr/bin/env python3

def main():
    pass

class Solution:
    """Write a program to find the node at which the 
    intersection of two singly linked lists begins.
    """
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        delta = 0
        markA = headA
        markB = headB
        if self._length(headA) > self._length(headB):
            delta = self._length(headA) - self._length(headB)
            for i in range(delta):
                markA = markA.next
        else:
            delta = self._length(headB) - self._length(headA)
            for i in range(delta):
                markB = markB.next
        while markA and markB:
            if markA == markB:
                return markA
            markA = markA.next
            markB = markB.next
        return None
        
    def _length(self, nodelist):
        if nodelist == None:
            return 0
        else:
            count = 0
            while nodelist:
                count += 1
                nodelist = nodelist.next
            return count

if __name__ == '__main__':
    main()