class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # build set as you incr row col square
        # row
        for row in board:
            seen_nums = set()
            for num in row:
                if num == '.':
                    continue
                if num in seen_nums:
                    return False
                else:
                    seen_nums.add(num)
        # col
        for col in range(len(board[0])):
            seen_nums = set()
            for row in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                elif num in seen_nums:
                    return False
                else:
                    seen_nums.add(num)

        #3x3
        #jump to square top left corner
        for sq_row in range(0,9,3):
            for sq_col in range(0,9,3):
                seen_nums = set()
                # scan 3x3 area from corner
                for row in range(sq_row, sq_row + 3):
                    for col in range(sq_col, sq_col + 3):
                        num = board[row][col]
                        if num == '.':
                            continue
                        elif num in seen_nums:
                            return False
                        else:
                            seen_nums.add(num)
        return True         
