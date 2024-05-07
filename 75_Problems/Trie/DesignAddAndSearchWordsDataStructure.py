#https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class DicNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_the_word = False

class WordDictionary(object):

    def __init__(self):
        self.dic = DicNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.dic
        for char in word:
            if char not in node.children:
                node.children[char] = DicNode()
            node = node.children[char]
        node.is_end_of_the_word = True
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(i, node):
            for i in range(i, len(word)):
                c = word[i]

                if c == ".":
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False

                    node = node.children[c]
            return node.is_end_of_the_word
        return dfs(0, self.dic)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
