'''
    https://leetcode.com/problems/combination-sum/solution/
    Time: O(N^(T/M)) N=len(candidates), T=target, M=smallest candidate
    Space: O(T/M)
'''
class Solution:
    def search(self, candidates, comb, rsum, ans, target):
        # found combination sum
        if rsum == target:
            ans.append(comb.copy())
            return
        
        for i in range(len(candidates)):
            if rsum + candidates[i] > target:
                # prune search
                break
            else:
                # make a decision
                rsum += candidates[i]
                comb.append(candidates[i])

            # call subroutine on reduced decision space
            self.search(candidates[i:], comb, rsum, ans, target)

            # backtrack
            rsum -= candidates[i]
            comb.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort candidates in ascending order
        candidates.sort()
        comb = []
        ans = []
        self.search(candidates, comb, 0, ans, target)
        return ans
        