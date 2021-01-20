# https://leetcode.com/problems/binary-search/

'''
    Algorithm: Binary Search
    - left and right pointers hold left and right indexes
    - get mid index between two
        - if # of elements is odd, it gets the middle index
        - if # of elements is even, it gets the left one --
        - NOTE: whether floor or ceil it doesnt matter
    - if mid holds the target value return
    - if target is greater than mid, move left to mid + 1
    - otherwise move right to mid - 1
    NOTE: left and right pointers are moved one space ahead or previous to 
    the mid index because the middle index is no longer needed
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((right + left) / 2)
            
            # mid is the number
            if nums[mid] == target:
                return mid
            
            # target is strictly greater than mid
            if target > nums[mid]:
                left = mid + 1
            # target is strictly less than mid
            else:
                right = mid - 1
        return -1
