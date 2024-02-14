#https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        final_set = []
        for i in range(len(nums)):
            if nums[i] <= target and nums[i] >= 0:
                for j in range(len(nums)):
                    if nums[i] + nums[j] == target and i != j:
                        final_set.append(i)
                        final_set.append(j)
                        return final_set
            if nums[i] > target and nums[i] < 0:
                for j in range(len(nums)):
                    if nums[i] + nums[j] == target and i != j:
                        final_set.append(i)
                        final_set.append(j)
                        return final_set
        """
        """
        for i in range(len(nums)):
            secondNumber = target - nums[i]
            for j in range(len(nums)):
                if secondNumber == nums[j] and i!=j:
                    return [i,j]
        """
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return[i, numMap[complement]]
