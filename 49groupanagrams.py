#Given an array of strings strs, group the anagrams
#together. You can return the answer in any order.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []

        curr_index = 0
        seen_strs = {}

        for i in range(len(strs)):
            current_word = strs[i]
            sorted_word = "".join(sorted(current_word))

            if sorted_word in seen_strs:
                index = seen_strs[sorted_word]
                result[index].append(current_word)

            else:
                seen_strs[sorted_word] = curr_index
                result.append([current_word])
                curr_index +=1

        return result
