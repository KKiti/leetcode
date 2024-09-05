# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        current_max = max(nums)

        if current_max <= 0:
            return current_max


        for i in range(len(nums)):
            if sum + nums[i] > 0:
                sum += nums[i]
            else:
                sum = 0

            if sum > current_max:
                current_max = sum
        return current_max
