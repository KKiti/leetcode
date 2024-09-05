# Given an integer x, return true if x is a
# palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nums = [d for d in str(x)]
        nums_rev = nums[::-1]
        middle = int(len(nums)/2)

        for i in range(middle):
            if nums[i] != nums_rev[i]:
                return False
        return True
