# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    NOTE: THIS SOLUTION DOESNT TRAVERSE THE TREE IN A ZIG 
    ZAG ORDER IT SIMPLY MIMICS IT
    
    Algorithm: BFS Level order
        - Basic BFS level order traversal except
        currentLevel nodes are appended based on direction
    Time: O(N)
    Space: O(M) -- M = max # of nodes in a level
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        queue = deque([root])
        ans = []
        direction = 1
        while queue:
            currentLevel = deque()
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()
                if direction % 2 == 1:
                    currentLevel.append(node.val)
                else:
                    currentLevel.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currentLevel)
            direction += 1
        return ans
            
        