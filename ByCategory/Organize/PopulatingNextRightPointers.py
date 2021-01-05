'''
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    Level order iterative top down solution.
    Time: O(N)
    Space: O(1)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

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
