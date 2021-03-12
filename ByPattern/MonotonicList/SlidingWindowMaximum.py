# https://leetcode.com/problems/sliding-window-maximum/
'''
    Algorithm: Monotonic Deque
    - Keep a monotonic decreasing deque so that leftmost element is always max
    - For every iteration
        - Clean the array -- Remove any indexes that are not in window
        - Pop any right indexes whose value is less than the current value
        - append current value
        - add leftmost idx element to ans
    Time: O(N)
    Space: O(K)
'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic Decreasing deque
        d = deque()
        left, right = 0, -1
        # Process first K elements and initialize deque
        for i in range(k):
            while d and nums[i] > nums[d[right]]:
                d.pop()
            d.append(i)
        ans = [nums[d[left]]]
        # sliding window
        for i in range(k, len(nums)):
            # Remove any indexes not part of window
            while d and d[left] < (i-(k-1)):
                d.popleft()
            # Pop any right indexes whose value is less than the current value
            while d and nums[i] > nums[d[right]]:
                d.pop()
            # add current value
            d.append(i)
            # leftmost idx holds max of window
            ans.append(nums[d[left]])
        return ans
