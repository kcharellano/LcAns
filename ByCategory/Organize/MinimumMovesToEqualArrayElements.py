'''
    Sort nums and then sum over every element (element - min)
    Time: O(nlogn)
    Space: O(1)
'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in reversed(range(1, len(nums))):
            count += nums[i] - nums[0]
        return count