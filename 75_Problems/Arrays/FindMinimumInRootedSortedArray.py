#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        nums.sort()
        return nums[0]
        """
        left = 0
        right = len(nums)-1
        minn = nums[0]

        if nums[0] <= nums[right]:
            return nums[0]

        while left <= right:
            mid = (left+right) // 2
            if(nums[mid] >= minn):
                left = mid + 1
            else:
                minn = nums[mid]
                right = mid - 1
        return minn
