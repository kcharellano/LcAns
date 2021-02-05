# https://leetcode.com/problems/binary-tree-right-side-view/

'''
    Algorithm: Level Order Traversal
    - To get a rightside view of the tree, you need to get the rightmost node at every level
    - Do a level order traversal on the binary tree and 
    add the rightmost of the level to get a "right-side view"
    Time: O(N)
    Space: O(2^d)
'''
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None: return []
        queue = deque([root])
        ans = []
        levelSize = 1
        while queue:
            ans.append(queue[-1].val)
            parentSize = levelSize
            levelSize = 0
            for i in range(parentSize):
                node = queue.popleft()
                if node.left:
                    levelSize += 1
                    queue.append(node.left)
                if node.right:
                    levelSize += 1
                    queue.append(node.right)
        return ans