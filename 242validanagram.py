# Given two strings s and t, return true if t is an anagram
# of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}

        if len(s) != len(t):
            return False

        for let in s:
            if let in letters:
                letters[let] +=1
            else:
                letters[let] =1

        for let in t:
            if let in letters and letters[let] > 0:
                letters[let] -= 1
            else:
                return False

        return True
