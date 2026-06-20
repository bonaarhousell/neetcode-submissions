class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(9):
            seen = set()
            for r in range(9):
                if board[col][r] == ".":
                    continue
                
                if board[col][r] in seen:
                    return False
                seen.add(board[col][r])

        for row in range(9):
            seen = set()
            for c in range(9):
                if board[c][row] == ".":
                    continue
                
                if board[c][row] in seen:
                    return False
                seen.add(board[c][row])

        for square in range(9):
            seen = set()
            for c in range(3):
                for r in range(3):
                    col = (square // 3) * 3 + c
                    row = (square % 3) * 3 + r
                    if board[col][row] == ".":
                        continue
                    
                    if board[col][row] in seen:
                        return False
                    seen.add(board[col][row])
        return True