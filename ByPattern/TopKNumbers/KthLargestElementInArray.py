# https://leetcode.com/problems/kth-largest-element-in-an-array

'''
    Algorithm: Kth largest element
        - Use a minheap to constantly keep track of the kth largest element
        - keep the minheap below a certain size
        - if size capacity reached
            - if new element is >= minimum element in minheap
            - pop min and add new element. (>= to deal with duplicates)
    Time: O(N*logK), N = amount of element, K = how many elements we store in heap
    Space: O(logK) -- size of heap 
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        size = 0
        for num in nums:
            if size < k:
                heapq.heappush(minheap, num)
                size += 1
            else:
                if num >= minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, num)
        return minheap[0]
        