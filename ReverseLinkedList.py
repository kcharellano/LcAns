# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    Single pass, iterative solution
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        # prev, current, next
        prev = None
        current = head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev