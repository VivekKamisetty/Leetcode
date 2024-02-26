#https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        def sort_words(strs):
            sorted_strs = []
            for word in strs:
                sorted_word = "".join(sorted(word))
                sorted_strs.append(sorted_word)
            return sorted_strs

        sorted_strs = list(sort_words(strs))

        for i in range(len(strs)):
            sorted_word = sorted_strs[i]
            if sorted_word not in dic:
                dic[sorted_word] = [strs[i]]
            else:
                dic[sorted_word].append(strs[i])

        print(dic)

        return list(dic.values())
