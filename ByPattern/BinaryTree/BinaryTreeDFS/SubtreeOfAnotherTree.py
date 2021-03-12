# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    Algorithm: Binary Tree DFS
    - Search every node in BT
    - Starts a subtree comparison for every node
    Time: O(N * ?)
    Space: O(N)
'''
class Solution:
    def subtreeComp(self, s, t):
        if s == None and t == None:
            return True
        elif s == None or t == None:
            return False
        elif s.val == t.val:
            return self.subtreeComp(s.left, t.left) and self.subtreeComp(s.right, t.right)
        else:
            return False
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.subtreeComp(s, t):
            return True
        
        if s.left and self.isSubtree(s.left, t):
            return True
        
        if s.right and self.isSubtree(s.right, t):
            return True
        
        return False
            