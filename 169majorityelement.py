# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = {}
        x = len(nums)/2 if len(nums)%2==0 else len(nums)/2 + 1

        for num in nums:
            if num in count:
                count[num] +=1
                if count[num] >= x:
                    return num
            else:
                count[num] =1

        return nums[0]
