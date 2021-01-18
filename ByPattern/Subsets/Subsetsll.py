# https://leetcode.com/problems/subsets-ii/

'''
    Algorithm: Subsets -- duplicate variation
        - Same subsets pattern as in subset.py
        - To adapt to an input list with possible duplicates 
        the array must first be sorted so that all duplicates are next to eachother in the list
        - Iterate over the input list as in regular subset pattern
        - Iterate over subset list but if elem has been seen before(duplicate)
        then the iteration over the subset list starts at the index where the 
        last element started instead of 0.
    Time: O(2^N)
    Space: O(2^N)
'''
from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        ansLen = 1
        # stores last starting place of element in subset list
        lastStart = defaultdict(int)
        
        for i in range(len(nums)):
            elem = nums[i]
            start = lastStart[elem]
            prevLen = ansLen
            for ii in range(start, ansLen):
                ans.append(ans[ii] + [elem])
                ansLen += 1
            lastStart[elem] = prevLen
        return ans
                