'''
    https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

'''
    Algorithm: Remove max and min
        - remove max between nums1 and nums2
        - remove min betwen nums1 and nums 2
        - Repeat until you are only left with < 3 numbers
        - remaning numbers are your medians
        - NOTE: both operations above take O(1) time because arrays are sorted
    Time: O(m+n)
    Space: O(1) --> don't need to use deque but I do for optimization reasons
'''
from collections import deque
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        deq1 = deque(nums1)
        deq2 = deque(nums2)
        rsum = 0
        while size1 + size2 > 2:
            # remove min
            if deq1 and deq2:
                if deq1[0] < deq2[0]:
                    deq1.popleft()
                    size1 -= 1
                else:
                    deq2.popleft()
                    size2 -= 1
            elif deq1:
                deq1.popleft()
                size1 -= 1
            elif deq2:
                deq2.popleft()
                size2 -= 1            
            # remove max
            if deq1 and deq2:
                if deq1[-1] > deq2[-1]:
                    deq1.pop()
                    size1 -= 1
                else:
                    deq2.pop()
                    size2 -= 1
            elif deq1:
                deq1.pop()
                size1 -= 1
            elif deq2:
                deq2.pop()
                size2 -= 1            
        if deq1 and deq2:
            rsum = float((deq1[0] + deq2[0]) / 2)
        elif deq1:
            if len(deq1) == 2:
                rsum = float((deq1[0] + deq1[1]) /2)
            else:
                rsum = float(deq1[0])
        elif deq2:
            if len(deq2) == 2:
                rsum = float((deq2[0] + deq2[1]) / 2)
            else:
                rsum = float(deq2[0])
        return rsum
        