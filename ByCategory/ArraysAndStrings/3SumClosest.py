# https://leetcode.com/problems/3sum-closest/

'''
    Algorithm: Two pointers left right variation
        - Sort numbers
        - Fix one number
        - Peform two pointers to look for closest 3sum to target
    Time: O(N^2)
    Space: O(1)
'''
from math import inf
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lastDiff = inf
        n = len(nums)
        ans = 0
        for i in range(n):
            left = i+1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(target - sum) < abs(lastDiff):
                    lastDiff = target - sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
                if lastDiff == 0:
                    break
        return target - lastDiff
            
        