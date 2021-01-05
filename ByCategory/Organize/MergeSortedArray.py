'''
    Create a copy of nums1 and then interweave minimums into nums1
    Time: O(M + N)
    Space: O(M)

    Note: To achieve a space complexity of O(1) one could start from the right side. 
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # copy nums1
        nums1Copy = [nums1[i] for i in range(m)]
        
        # pointers to indexes of nums2 and nums1Copy
        p1 = 0
        p2 = 0

        # pointer to index of nums1
        i = 0

        # interweave minimum of [p1] and [p2]
        while p1 < m and p2 < n:
            if nums1Copy[p1] < nums2[p2]:
                nums1[i] = nums1Copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
            i += 1
        
        # fill remaining
        if p1 < m:
            while p1 < m:
                nums1[i] = nums1Copy[p1]
                p1 += 1
                i += 1
        elif p2 < n:
            while p2 < n:
                nums1[i] = nums2[p2]
                p2 += 1
                i += 1