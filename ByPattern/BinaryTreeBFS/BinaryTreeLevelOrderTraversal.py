# https://leetcode.com/problems/binary-tree-level-order-traversal

'''
    Algorithm: BFS Level Order
    Time: O(N) -- Processes all nodes in tree
    Space: O(M) where M = maximum number of nodes in any given level
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        
        q = deque([root])
        ans = []
        while q:
            levelSize = len(q)
            currentLevel = []
            # pop all nodes on current level
            for _ in range(levelSize):
                node = q.popleft()
                currentLevel.append(node.val)
                
                # Fill queue with next level nodes
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            ans.append(currentLevel)
        return ans
