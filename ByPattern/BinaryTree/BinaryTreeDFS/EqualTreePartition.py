# https://leetcode.com/problems/equal-tree-partition/
'''
    Algorithm: 
    - Record the sum of all subtrees in the original tree
        - You can do this recursively using DFS
    - If totalSum / 2 exists in the sumList then there exists a solution
    Time: O(N)
    Space: O(N)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumDfs(self, node, sumList):
        if node == None: return 0
        sum = node.val + self.sumDfs(node.left, sumList) + self.sumDfs(node.right, sumList)
        sumList.append(sum)
        return sum
    
    def checkEqualTree(self, root: TreeNode) -> bool:
        sumList = []
        totalSum = self.sumDfs(root, sumList)
        sumList.pop()
        return (totalSum / 2.0) in sumList