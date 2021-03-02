'''
    Algorithm: 3 Ptr Weaving
    - Maintain the inequality prev -> min(p1, p2) -> max(p1, p2)
    - Weave ptrs based on value since they are sorted
    - quit once any ptr points to none. No need to keep going
    Time: O(L1 + L2)
    Space: O(1)

    Other approches: 
    - build 2 lists from l1 and l2
    - Concatenate them into a list l3 and sort l3
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(-1)
        prev = sentinel
        p1, p2 = l1, l2
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                # connect prev to p1
                prev.next = p1
                # hold a temp ptr to p1.next
                temp = p1.next
                # point p1 to p2
                p1.next = p2
                # move p1 to its original next neighbor
                p1 = temp
                # move prev ptr up one
                prev = prev.next
            else:
                prev.next = p2
                temp = p2.next
                p2.next = p1
                p2 = temp
                prev = prev.next
        return sentinel.next