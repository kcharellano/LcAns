"""
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
    Level Order top down iterative solution
    Time: O(N)
    Space: O(2^logN) -- in the worse case we are storing this many nodes in a list

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
            return root
        
        currentlevel = [root]
        while currentlevel:
            # form list of nodes in the next level
            nextLevel = []
            for node in currentlevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            # connect nextLevel nodes
            for i in range(len(nextLevel)-1):
                nextLevel[i].next = nextLevel[i+1]
            # set level to nextLevel
            currentlevel = nextLevel
        return root

