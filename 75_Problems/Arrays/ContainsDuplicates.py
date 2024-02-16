#https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        dict = {}
        for i in range(len(nums)):
            dict[i] = nums[i]

        my_dict = list(dict.values())
        my_dict.sort()

        for i in range(len(my_dict) - 1):
            if my_dict[i] == my_dict[i+1]:
                return True
        return False
        """

        nums_len = len(nums)
        nums_set = set(nums)

        print(len(nums_set))

        if (len(nums) == len(nums_set)):
            return False
        else:
            return True      
