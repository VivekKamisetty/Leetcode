#https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/930908104/
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            if(self.check(words[i], allowed) == 1):
                count+=1
                #print(words[i])
        return count

    def check(self,word, allowed):
        #print(word, allowed)
        wordcount = 0
        flag = 0
        for i in range(len(word)):
            for j in range(len(allowed)):
                if(word[i]) == allowed[j]:
                    wordcount = wordcount + 1
            if wordcount == len(word):
                flag = 1
        return flag
