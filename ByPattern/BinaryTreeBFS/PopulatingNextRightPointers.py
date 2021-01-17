
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
# class Node:
#    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#        self.val = val
#        self.left = left
#        self.right = right
#        self.next = next

'''
    Algorithm: Level Order Traversal -- Variation
    - Using the fact that the tree is a perfect tree we there is always atleast a left most node
    - Traverse tree level by level starting with the leftmost node on any level
        - if the left most node is null then the level empty as well so stop
        - otherwise, iterate through nodes in level and connect all their children
        - then move on the the next level
    Time: O(N) -- this algorithm goes through all the nodes
    Space: O(1)
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        node = root
        while node.left:
            # connect all children nodes
            cursor = node
            while cursor:
                cursor.left.next = cursor.right
                if cursor.next:
                    cursor.right.next = cursor.next.left
                cursor = cursor.next
            # move node to the next level
            node = node.left
        return root
