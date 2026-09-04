class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # build set as you incr row col square
        # row
        for row in board:
            seen = set()
            for num in row:
                if num == '.':
                    continue
                elif num in seen:
                    return False
                else:
                    seen.add(num)
        # col
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                elif num in seen:
                    return False
                else:
                    seen.add(num)

        #3x3
        #jump to square top left corner
        for sqrow in range(0,9,3):
            for sqcol in range(0,9,3):
                seen = set()
                for row in range(sqrow, sqrow + 3):
                    for col in range(sqcol, sqcol + 3):
                        num = board[row][col]
                        if num == '.':
                            continue
                        elif num in seen:
                            return False
                        else: 
                            seen.add(num)
        return True