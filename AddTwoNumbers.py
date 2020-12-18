# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    Elementary math approach.
    Time: O(N)
    Space: O(N)
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        carry = 0
        sentinel = ListNode(-1)
        tail = sentinel
        while p1 != None or p2 != None:
            # get the integer value of each node
            val1 = p1.val if p1 != None else 0
            val2 = p2.val if p2 != None else 0
            # sum them and take care of carry
            valSum = val1 + val2 + carry
            if valSum > 9:
                carry = 1
                valSum -= 10
            else:
                carry = 0
            # append to answer list
            tail.next = ListNode(valSum)
            tail = tail.next

            # increment pointers
            p1 = p1.next if p1 != None else None
            p2 = p2.next if p2 != None else None
        
        if carry:
            tail.next = ListNode(carry)
        return sentinel.next

            

