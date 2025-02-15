# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


def mergeAlternately(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    result = [let for let in word1]
    len2 = len(word2)

    j=1

    for let in word2:
        result.insert(j, let)
        j+=2

    return ''.join(result)
