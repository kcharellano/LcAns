'''
    Algorithm: Heap Weaving
    - Create a heap out of k ptrs 
    - Insert the min of th k ptrs at all times
    Time: O(N*logK), k = # ofs lists, N = Nodes in the final linked lists
    Space: O(N + K)
'''
import heapq

# heapq is a minheap by default
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # create heap from all lists nodes (val, tb, ptr)
        minheap = []
        for tb, ptr in enumerate(lists):
            if ptr != None:
                minheap.append((ptr.val, tb, ptr))
        heapq.heapify(minheap)
        resHead = ListNode(-1)
        resPtr = resHead
        # weave k ptrs
        while minheap:
            # pop the min
            val, tb, ptr = heapq.heappop(minheap)
            # append to result
            resPtr.next = ListNode(val)
            resPtr = resPtr.next
            # add the next node to heap if not null
            if ptr.next != None:
                heapq.heappush(minheap, (ptr.next.val, tb, ptr.next))
        return resHead.next
