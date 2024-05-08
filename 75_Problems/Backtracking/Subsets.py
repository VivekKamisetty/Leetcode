#https://leetcode.com/problems/subsets/
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def bt(curr, start):
            if len(nums) == start:
                res.append(list(curr))
                return
            
            curr.append(nums[start])
            bt(curr, start+1)

            curr.pop()

            bt(curr, start+1)

        bt([], 0)
        return res
