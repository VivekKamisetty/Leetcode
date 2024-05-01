#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        mini = 5001

        while left <= right:
            mid = (left + right) // 2
            mini = min(mini, nums[mid])

            if nums[mid] < nums[right]:
                right = mid - 1
                mini = min(mini, nums[mid])

            elif nums[mid] > nums[right]:
                left = mid + 1
                mini = min(mini, nums[mid])

            else:
                right -= 1
                
        return mini        

        
