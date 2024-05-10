#https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(candidates)

        def bt(curr, i):

            if sum(curr) == target:
                res.append(list(curr))
                return

            if sum(curr) > target:
                return

            for j in range(i, len(candidates)):                   
                curr.append(candidates[j])
                bt(curr, j)
                curr.pop()

        bt([], 0)
        return res
