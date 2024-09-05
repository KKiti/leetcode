# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):

            remainder = target - nums[i]
            if remainder in nums[i+1:len(nums)]:

                y = nums[i+1:len(nums)].index(remainder)
                y = y+i+1

                return [i, y]
            i+=1
