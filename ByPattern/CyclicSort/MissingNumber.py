# https://leetcode.com/problems/missing-number

'''
    NOTE: This solution is only optimal with the given constraints:
        - constant extra space
        - O(N) time
    Algorithm: Cyclic Sort
        - pass1: Sort elements using cyclic sort
        - pass2: return index that doesn't match value of len(nums)
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        end = len(nums)
        # cyclic sort
        while i < end:
            elem = nums[i]
            # if the element is a valid index and
            # not in the right spot
            if elem != end and i != elem:
                # place element into correct index by swapping
                nums[elem], nums[i] = elem, nums[elem]
            else:
                i += 1
        
        for i in range(end):
            if i != nums[i]:
                return i
        return end
                
                