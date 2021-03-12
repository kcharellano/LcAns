# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
    Algorithm: Bidirectional Search in Binary Tree + BFS
    - Create a mapping of every child to its parent
    - Perform a regular BFS starting from the target node
    
    Time: O(N)
    Space: O(N)
'''
from collections import deque
class Solution:
    def dfs(self, parent, child, parentOf):
        parentOf[child] = parent
        
        if child.left:
            self.dfs(child, child.left, parentOf)
        
        if child.right:
            self.dfs(child, child.right, parentOf)
                
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # get the parent of each node in the binary tree
        parentOf = {}
        self.dfs(None, root, parentOf)
        
        queue = deque()
        ans = []
        # (node, stepsFromTarget)
        queue.append((target, 0))
        visited = set()
        # perform BFS from target node
        while queue:
            node, steps = queue.popleft()
            
            if steps == K:
                ans.append(node.val)
                continue
            
            # add neighbors of node to queue
            if parentOf[node] != None and parentOf[node] not in visited:
                queue.append((parentOf[node], steps+1))
                
            if node.left and node.left not in visited:
                queue.append((node.left, steps+1))
                
            if node.right and node.right not in visited:
                queue.append((node.right, steps+1))
            
            visited.add(node)
            
        return ans