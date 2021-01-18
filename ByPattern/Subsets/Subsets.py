# https://leetcode.com/problems/subsets -- i.e generate the power set

'''
    Algorithm: Subsets
    - keep a list of all subsets so far
    - For every element
        - for every subset, append the subset + element
    Time: O(2^N) -- a set with N elements will have a powerset with 2^N elements
    Space: O(2^N) -- storing all subsets
    Note: Works because of no duplicates
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        size = 1
        for num in nums:
            for i in range(size):
                ans.append([num] + ans[i])
                size += 1
        return ans
