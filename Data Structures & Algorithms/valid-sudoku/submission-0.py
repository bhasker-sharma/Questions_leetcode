class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check all 9 rows
        for r in range(9):
            seen = set()
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
                
        #check all 9 coloums
        for c in range(9):
            seen = set()
            for r in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
                
        #check in matrix 
        for box_r in range(0,9,3):
            for box_c in range(0,9,3):
                seen =set()
                for r in range(box_r,box_r+3):
                    for c in range(box_c,box_c+3):
                        cell = board[r][c]
                        if cell == ".":
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)
        return True
            