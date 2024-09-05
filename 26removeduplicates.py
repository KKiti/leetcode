# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 1
        curr_value = nums[0]

        for j in range(1, len(nums)):
            if nums[j] != curr_value:
                nums[index] = nums[j]
                curr_value = nums[j]
                index += 1

        # print(nums)
        return index
