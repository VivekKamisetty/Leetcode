#https://leetcode.com/problems/subsets-ii/description/

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        def bt(i, curr):
            if curr not in res:
                res.append(list(curr))

            if len(curr) > len(nums):
                return 

            for j in range(i, len(nums)):
                curr.append(nums[j])
                bt(j+1, curr)
                curr.pop()
        bt(0, [])
        return res
            

            
