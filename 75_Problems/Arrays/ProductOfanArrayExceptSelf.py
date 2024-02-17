#https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = [1]*len(nums)

        prod = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= prod
            prod *= nums[i]

        prod = 1
        for i in range(len(nums)):
            answer[i] *= prod
            prod *= nums[i]
        return answer

        
        """answer = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            val = nums[i]
            nums.remove(val)
            print(nums)
            for j in range(len(nums)):
                prod *= nums[j]
                print(nums[j])
            #print(prod)
            answer[i] = prod
            nums.insert(i,val)
            prod = 1
        return answer"""
            
