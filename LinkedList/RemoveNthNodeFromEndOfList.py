'''
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
'''

'''
    Algorithm:
        - 2 node pointers, nodeA and nodeB
        - nodeA goes all the way to end of list
        - nodeB stays n spaces away from nodeA and is also always behind the node that is to be deleted
        - After nodeA reaches the end simply delete the node after nodeB
        - Edgecase: if the node to be deleted is the head then just return head.next
    Time: O(N)
    Space: O(1)
    24min
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentinel = ListNode(-1, head)
        nodeB = sentinel
        nodeA = sentinel
        delay = n
        count = 0
        while nodeA.next != None:
            if count < delay:
                nodeA = nodeA.next
                count += 1
            else:
                nodeB = nodeB.next
                nodeA = nodeA.next
        
        deleteNode = nodeB.next
        if deleteNode is head:
            return head.next
        else:
            nodeB.next = deleteNode.next
            deleteNode.next = None
            return head