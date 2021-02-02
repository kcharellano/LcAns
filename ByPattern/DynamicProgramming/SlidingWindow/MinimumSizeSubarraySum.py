'''
    Algorithm: Dynamic Sliding Window
        - expand right until rsum < target
        - shrink left while rsum >= target
    Time: O(N)
    Space: O(1)
'''
from math import inf
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        left = 0
        rsum = 0
        target = s
        count = 0
        for right in range(n):
            # expand rsum < target
            rsum += nums[right]
            count += 1
            # shrink rsum while rsum >= target
            while rsum >= target:
                ans = min(ans, count)
                rsum -= nums[left]
                left += 1
                count -= 1
        return ans if ans != inf else 0