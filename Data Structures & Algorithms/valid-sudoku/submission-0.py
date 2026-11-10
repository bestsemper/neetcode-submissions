class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Horizontal
        for r in range(9):
            horizontal = set()
            for c in range(9):
                val = board[r][c]
                if val in horizontal and val != '.':
                    return False
                horizontal.add(val)
        # Check Vertical
        for c in range(9):
            vertical = set()
            for r in range(9):
                val = board[r][c]
                if val in vertical and val != '.':
                    return False
                vertical.add(val)
        # Check Boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = set()
                for rshift in range(3):
                    for cshift in range(3):
                        val = board[r+rshift][c+cshift]
                        if val in box and val != '.':
                            return False
                        box.add(val)
        return True