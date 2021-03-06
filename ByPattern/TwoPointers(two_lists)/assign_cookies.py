'''
    Algorithm: Greedy Assignment
    - give each child the smallest size cookie they will accept 
    to satisfy as many children as possible
'''
class Solution:
    # assume both g and s are sorted in ascending order
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                cookie += 1
                child += 1
            else:
                cookie += 1
        return child