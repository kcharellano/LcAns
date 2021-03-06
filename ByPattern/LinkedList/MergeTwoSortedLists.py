# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# prevNode is needed to correct interweaving
# in case where a value in list A is greater than two 
# consecutive values in list B
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        sentinel = ListNode(-1)
        prevNode = sentinel
        while l1 and l2:
            if l1.val > l2.val:
                prevNode.next = l2
                temp = l2.next
                l2.next = l1
                l2 = temp
                prevNode = prevNode.next
            else:
                prevNode.next = l1
                temp = l1.next
                l1.next = l2
                l1 = temp
                prevNode = prevNode.next
        return sentinel.next