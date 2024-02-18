#https://leetcode.com/problems/maximum-product-subarray/description/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resultProd = nums[0]
        maxProd = nums[0]
        minProd = nums[0]

        """for i in nums[1:]:
            minProd = min(i, currentProd*i)
            currentProd = max(i , currentProd*i)
            maxProd = max(maxProd, currentProd, )
        return maxProd"""

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxProd, minProd = minProd, maxProd
            minProd = min(nums[i], minProd*nums[i])
            maxProd = max(nums[i] , maxProd*nums[i])
            resultProd = max(maxProd, resultProd)
        return resultProd
