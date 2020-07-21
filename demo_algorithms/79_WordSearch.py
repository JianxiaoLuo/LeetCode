# My solution, cannot work

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.width = len(board[0])
        self.height = len(board)
        self.w_len = len(word)
        self.word = word
        self.flag = False
        self.board = board
        self.board_copy = board.copy()
        
        for i in range(self.height):
            for j in range(self.width):
                if board[i][j] == word[0]:
                    self.board_copy = board[:]
                    print(id(self.board_copy), id(self.board), id(board))
                    print(self.board_copy, self.board)
                    print("-----------New-----------")
                    self.dfs(i, j, 0)
                    if self.flag: return True
                    else: continue
        return False
    
    def dfs(self, i, j, index):
        if i >= 0 and i < self.height and j >= 0 and j < self.width:
            if self.board_copy[i][j] == self.word[index]:
                if index == self.w_len-1:
                    self.flag = True
                    return True
                self.board_copy[i][j] = '$'
                if self.dfs(i-1, j, index+1) or self.dfs(i+1, j, index+1) or self.dfs(i, j-1, index+1) or self.dfs(i, j+1, index+1):                 
                    return True
        if self.flag:
            return 
        return 
