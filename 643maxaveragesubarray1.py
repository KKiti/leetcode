# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k
# that has the maximum average value and return this value.

# Any answer with a calculation error less than 10-5 will be accepted.

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #get starting average
        currentavg = 0
        for i in range(k):
            currentavg  += nums[i]

        if n == k:
            return float(currentavg)/k

        for i in range(k, len(nums)):
            diff += (nums[i] - nums[i-k])
            if diff > 0:
                currentavg += diff
                diff = 0

        return float(currentavg)/k
