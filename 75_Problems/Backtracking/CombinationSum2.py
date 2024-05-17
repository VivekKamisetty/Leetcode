#https://leetcode.com/problems/combination-sum-ii/description/

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = sorted(candidates)
        def bt(curr, start, targetSum):
            if targetSum == target:
                res.append(list(curr))
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if targetSum + candidates[i] > target:
                    break
                curr.append(candidates[i])
                bt(curr, i+1, targetSum + candidates[i])
                curr.pop()

        bt([], 0, 0)
        return res
