# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
#     Choose a star in s.
#     Remove the closest non-star character to its left, as well as remove the star itself.
#
# Return the string after all stars have been removed.
#
# Note:
#
#     The input will be generated such that the operation is always possible.
#     It can be shown that the resulting string will always be unique.

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = s[::-1]
        res=""

        count = 0
        for char in str:
            if char == "*":
                count += 1
            else:
                if count > 0:
                    count -=1
                else:
                    res = char + res
        return res


    def removeStarsStack(self, s):
        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
