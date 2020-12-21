'''
    https://leetcode.com/problems/permutations/
    Time: O(N!)
    Space: O(?)
'''
class Solution:
    def findPerms(self, choices, perm, ans):
        # if no more choices we have constructed a permuation
        if not choices:
            ans.append(perm[:])
            return
        
        for choice in choices:
            # choose an element
            perm.append(choice)
            
            # reduce decision space
            reducedChoices = choices.copy()
            reducedChoices.remove(choice)
            
            # call subroutine
            self.findPerms(reducedChoices, perm, ans)

            # backtrack
            perm.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        choices = set(nums)
        perm = []
        ans = []
        self.findPerms(choices, perm, ans)
        return ans