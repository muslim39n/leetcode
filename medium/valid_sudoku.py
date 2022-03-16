class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    ij = i + 1
                    while ij < 9:
                        if board[ij][j] == board[i][j]:
                            return False

                        ij += 1

                    ij = j + 1
                    while ij < 9:
                        if board[i][ij] == board[i][j]:
                            return False

                        ij += 1

        for mi in range(1, 9, 3):
            for mj in range(1, 9, 3):
                used = [False] * 10

                for i in range(mi - 1, mi + 2):
                    for j in range(mj - 1, mj + 2):
                        if board[i][j] != '.':
                            if used[int(board[i][j])]:
                                return False

                            used[int(board[i][j])] = True

        return True

        
