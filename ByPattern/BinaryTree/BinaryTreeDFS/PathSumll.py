# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    Algorithm: Binary Tree DFS with path tracker
    Time: O(N)
    Space: O(logN)    
'''
class Solution:
    def dfs(self, node, target, rsum, path, ans):
        if node.left == None and node.right == None:
            if rsum + node.val == target:
                path.append(node.val)
                ans.append(path[:])
                path.pop()
                return
            
        if node.left:
            path.append(node.val)
            self.dfs(node.left, target, rsum + node.val, path, ans)
            path.pop()
        
        if node.right:
            path.append(node.val)
            self.dfs(node.right, target, rsum + node.val, path, ans)
            path.pop()
            
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        self.dfs(root, sum, 0, [], ans)
        return ans
        