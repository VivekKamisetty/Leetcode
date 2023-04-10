#https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        result = []
        for i in range(len(nums)):
            result.append(self.funct(nums, i))
        return result
    
    def funct(self, nums, i):
        result = 0
        for j in range(len(nums)):
            result += abs(nums[i] - nums[j])
        return result
