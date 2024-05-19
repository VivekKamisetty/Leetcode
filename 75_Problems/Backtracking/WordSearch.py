#https://leetcode.com/problems/word-search/description/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        max_i = len(board)
        max_j = len(board[0])
        def bt(i, j, index):
            
            if index == len(word):
                return True
            
            if max_i <= i or max_j <= j or i < 0 or j < 0 or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for dx, dy in directions:
                if bt(i + dx, j + dy, index + 1):
                    return True
            
            board[i][j] = temp
            return False
        for i in range(max_i):
            for j in range(max_j):
                if bt(i, j, 0):
                    return True
        return False
