'''
    https://leetcode.com/problems/copy-list-with-random-pointer/
'''


'''
    Algorithm: 2 pass
        - 1st pass forms the copy list with next nodes and maps original nodes to indexes
        - 2nd pass connect random nodes for the copy list
    Time: O(N)
    Space: O(N)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        sentinel = Node(-1)
        copy = sentinel
        node = head
        indexMap = {}
        copyIndexMap = {}
        
        # 1st pass that establishes next nodes and maps indexes to nodes
        index = 0
        while node != None:
            copy.next = Node(node.val)
            copy = copy.next
            indexMap[node] = index
            copyIndexMap[index] = copy
            # increment node pointer
            node = node.next
            index+=1
        
        # 2nd pass established random node pointers
        node = head
        copy = sentinel.next
        while node != None:
            if node.random != None:
                copy.random = copyIndexMap[indexMap[node.random]]
            node = node.next
            copy = copy.next
        
        return sentinel.next
        