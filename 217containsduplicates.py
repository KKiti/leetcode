# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_nums = set(nums)

        if len(set_nums) < len(nums):
            return True
        else:
            return False
        
