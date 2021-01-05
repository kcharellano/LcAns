# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    Algorithm:
        -Use DFS to find path to node P and node Q
        -Compare nodePaths and find their last common value starting from the root.
    Time: O(V+E)
    Space: O(logN)
'''
from collections import deque
class Solution:
    def dfs(self, currentNode, targetNode, path):
        if currentNode.val == targetNode.val:
            return True
        
        if currentNode.left:
            path.append(currentNode.left)
            if self.dfs(currentNode.left, targetNode, path):
                return True
            path.pop()

        if currentNode.right:
            path.append(currentNode.right)
            if self.dfs(currentNode.right, targetNode, path):
                return True
            path.pop()

        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # get path from root to node p
        pPath = [root]
        self.dfs(root, p, pPath)
        
        # get path from root ot node q
        qPath = [root]
        self.dfs(root, q, qPath)

        # find lowest common ancestor
        lastCommon = None
        for i in range(min(len(pPath), len(qPath))):
            if pPath[i] != qPath[i]:
                return lastCommon
            else:
                lastCommon = pPath[i]
        return lastCommon
    
    def printNodes(self, ls):
        for node in ls:
            print(node.val, end="")
        print()

'''
    Algorithm: Euler's Tour
        - Use DFS to create a tree traversal arrray
        - Find the minimum depth node between nodes p and q inclusive
        - NOTE: Unfinished
'''

class Solution:
    def appendTraversal(self, idList, depthList, id, depth):
        depthList.append(depth)
        idList.append(id)

    def dfs(self, idList, depthList, currentNode, depth):
        self.appendTraversal(idList, depthList, currentNode.val, depth)       
        if currentNode.left:
            self.dfs(idList, depthList, currentNode.left, depth+1)
            self.appendTraversal(idList, depthList, currentNode.val, depth)       
        if currentNode.right:
            self.dfs(idList, depthList, currentNode.right, depth+1)
            self.appendTraversal(idList, depthList, currentNode.val, depth)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        idList = []
        depthList = []
        self.dfs(idList, depthList, root, 0)
        
        for nodeId, depth in zip(idList, depthList):
            pass

'''
    Algorithm: Tarjan's Offline LCA
    -- fuck this algorithm
'''