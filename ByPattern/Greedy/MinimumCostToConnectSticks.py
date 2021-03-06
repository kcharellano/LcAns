'''
    Algorithm: Greedy
    - choose the smallest 2 stick to pair until only one stick is left
    Time: O(nLogn)
    Space: O(1)
'''

import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        size = len(sticks)
        heapq.heapify(sticks)
        
        cost = 0
        while size > 1:
            # pop 2 min sticks
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            cost += (a+b)
            # add combined stick back to heap
            heapq.heappush(sticks, (a+b))
            size -= 1
        return cost
