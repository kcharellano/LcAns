# https://leetcode.com/problems/path-sum-iii/

'''
    Algorithm: Binary Tree DFS with Memoization
        - Traverse tree in DFS fashion
        - store running sum paths from root to node during traversal
        - When processing a node, if a valid path exists in current path, 
        then the cache will contain[rsum - target]
        - Add this to the result, update the cache with rsum and recurse,
        - When a path bactracks, remove(i.e decrement its frequency) from the
        cache because it can no longer be used.
'''
class Solution:
    def dfs(self, node, target, rsum, cache):
        # basecase
        if node == None:
            return
        
        # add node val to current path sum
        rsum += node.val
        # if a valid path exists in the current path, oldSum will be in the cache
        oldrsum = rsum - target
        # update result
        self.ans += cache.get(oldrsum, 0)
        # add current path to cache
        cache[rsum] = cache.get(rsum, 0) + 1
        
        self.dfs(node.left, target, rsum, cache)
        self.dfs(node.right, target, rsum, cache)
        # backtrack and remove this rsum from cache
        cache[rsum] -= 1
        
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        cache = {0: 1}
        
        self.dfs(root, sum, 0, cache)
        return self.ans

# another version
from collections import defaultdict
class Solution:
    def dfs(self, node, cache, rsum, k):
        if node == None:
            return
        
        # add current node to prefix sum
        rsum += node.val
        
        # check if valid path exists in current path
        self.count += cache[rsum-k]
        
        # add prefix sum to cache
        cache[rsum] += 1
        
        # dfs search
        self.dfs(node.left, cache, rsum, k)
        self.dfs(node.right, cache, rsum, k)
        
        # backtrack -- remove current path to 
        cache[rsum] -= 1
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        cache = defaultdict(int)
        cache[0] = 1
        self.dfs(root, cache, 0, sum)
        return self.count
        
        