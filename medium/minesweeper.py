class Solution:
    def isMine(self, r, c):
        if r >= 0 and r < len(self.board) and c >= 0 and c < len(self.board[0]) and self.board[r][c] == 'M':
            return True

        return False


    def countAdjacentMines(self, r, c):
        cnt = 0

        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                cnt += self.isMine(i, j)

        return cnt


    def reveal(self, r, c):
        if r < 0 or c < 0 or r >= len(self.board) or c >= len(self.board[0]) or self.board[r][c] != 'E':
            return

        cnt = self.countAdjacentMines(r, c)
        if cnt == 0:
            self.board[r][c] = 'B'

            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    self.reveal(i, j)

        else:
            self.board[r][c] = str(cnt)




    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        self.board = board

        self.reveal(click[0], click[1])

        return self.board



        
