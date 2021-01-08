# https://leetcode.com/problems/3sum

'''
    Algorithm: Two sum one pass hash
        - Same as below solution except by
        using a hashset to search for complement instead
        of two pointer.
    Time: O(n^2)
    Space: O(n) -- for hashset
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

'''
    Algorithm: Two pointer -- left right variation
        - Sort array to avoid duplicates
            - Alternative -- store answers in a set and order them before to avoid duplicates 
        - Fix one index in array
        - Use two pointer pattern from left=index+1 and right=len(nums)-1 to find
        two values that when summed = -nums[index]
        Time: O(N^2)
        Space: O(1) -- not counting answer list
'''
class Solution:
    def twoSum(self, nums, index, n, ans):
        left = index+1
        right = n-1
        while left < right:
            csum = nums[left] + nums[right] + nums[index]
            if csum > 0:
                right -= 1
            elif csum < 0:
                left += 1
            else:
                ans.append([nums[left], nums[right], nums[index]])
                left += 1
                right -= 1
                # skip duplicates
                while left < right and nums[left] == nums[left-1]:
                    left += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                # remaining values are only postive, thus impossible
                # to sum to zero
                break
            # skip duplicates
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, n, ans)
        return ans
        
        