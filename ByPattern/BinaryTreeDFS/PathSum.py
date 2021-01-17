# https://leetcode.com/problems/path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    Algorithm: Binary Tree DFS Recursive
        - basic DFS
    Time: O(N)
    Space: O(logN) -- height of the tree
'''
class Solution:
    def dfs(self, node, target, rsum):
        if node.left == None and node.right == None:
            return True if rsum + node.val == target else False
        
        if node.left:
            if self.dfs(node.left, target, rsum + node.val):
                return True
        if node.right:
            if self.dfs(node.right, target, rsum + node.val):
                return True
        
        return False
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        return self.dfs(root, sum, 0)
        