# https://leetcode.com/problems/subarray-product-less-than-k/

'''
    Algorithm: Sliding Window
    - look at gdrive explanation
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

'''
    Algorithm: naive
    Time: O(n^2)
    Space: O(1)
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            #subarr = [nums[i]]
            prod = nums[i]
            if prod < k:
                ans += 1
            for j in range(i+1, n):
                #subarr.append(nums[j])
                prod *= nums[j]
                if prod < k:
                    ans += 1
                else:
                    break
        return ans