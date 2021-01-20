# https://leetcode.com/problems/search-in-rotated-sorted-array

'''
    Algorithm: Modified Binary Search
        - Find the pivot element using a modified binary search
        - Split the original list into two sorted sections
        - perform regular regular binary search on both sections
    Time: O(logN)
    Space: O(1)
'''
from math import floor
class Solution:
    def isStart(self, nums, numsLen, idx):
        # idx has a left and right element
        if idx + 1 < numsLen and nums[idx] > nums[idx+1]:
            return True
        # otherwise nums is a singleton list
        return False
    
    # modified binary search to find start of ascending sequence
    def findStart(self, nums, numsLen):
        left = 0
        right = numsLen - 1
        
        if nums[left] < nums[right] or numsLen == 1:
            return 0
        
        while left <= right:
            mid = floor((left + right) / 2)
            
            if self.isStart(nums, numsLen, mid):
                return mid + 1
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        # With valid input, this will never get returned
        return -1
    
    def binSearch(self, nums, left, right, target):
        while left <= right:
            mid = floor((left+right) / 2)
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # find pivot index
        numsLen = len(nums)
        pivot = self.findStart(nums, numsLen)
        
        #edgecase: pivot is target 
        if nums[pivot] == target:
            return pivot
        
        # split list into correctly sorted lists
        ans = self.binSearch(nums, 0, pivot-1, target)
        if ans != -1:
            return ans
        ans = self.binSearch(nums, pivot+1, numsLen-1, target)
        return ans
