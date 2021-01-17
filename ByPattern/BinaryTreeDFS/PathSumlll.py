# https://leetcode.com/problems/path-sum-iii/

'''
    Solution: Binary Tree DFS 2x
        - Have an outer Iterative DFS that goes through every node
        in the tree
        - For every node in the tree, call a recursive DFS that counts the number
        of "valid" path sums starting from that node
    Time: O(N^2)
    Space: O(logN)
'''
class Solution:
    def dfs(self, node, rsum, target):
        if node == None:
            return 0
        
        count = 0
        if rsum + node.val == target:
            count = 1
        
        leftCount = self.dfs(node.left, rsum + node.val, target)
        rightCount = self.dfs(node.right, rsum + node.val, target)
        return leftCount + rightCount + count
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        
        totalCount = 0
        stack = [root]
        while stack:
            curNode = stack.pop()
            totalCount += self.dfs(curNode, 0, sum)
            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)
        return totalCount
        