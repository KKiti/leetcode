# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

#    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

# Note that the integers in the lists may be returned in any order.

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        set1 = set(nums1)
        set2 = set(nums2)
        nums3 = list(set1 - set2)
        nums4 = list(set2 - set1)

        return [nums3, nums4]
