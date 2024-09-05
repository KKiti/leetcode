# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)

        while i < j:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                j-=1
            else:
                i+=1



# better solution using left and right pointers
# move all non-zeronumbers to the left by swapping
    def moveZeroesPointers(self,nums):
        #left pointer
        left = 0

        #right pointer moves across one by one
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                # once last left spot has been filled, move across again
                left += 1

        return nums
