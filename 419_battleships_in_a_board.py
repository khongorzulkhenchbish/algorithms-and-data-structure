class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        time: O(n) space(1) without modifying the given list
        max num of ships per board = max num of black/white cells in chessboard
        The trick is "Once we've found a top-left 'X', we found a battleship.
        1. Battleships are not contagious to each other / at least 1 row, col between, or diagonally distanced.
        2. Battleships are shaped as 1n or n1 rectangles.
        """
        if len(board) == 0: return 0
        row, col = len(board), len(board[0])
        counter = 0

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'X':
                    # first cell of the ship found
                    if (r == 0 or board[r-1][c] == '.') and (c == 0 or board[r][c-1]== '.'):
                        # only when the current cell is not part of any registered ship
                        counter += 1
        return counter
        """ given =>
        [X . X . X]
        [. X . X .]
        [X . X . X]
        row = 3, col = 5
        board[0][0] => count = 1
        board[0][2] => count = 2
        ...
        board[1][0] => count = 3 => board[1][1] => count = 4
        A .
        . X => to understand for ship to be countered, the upper and left cells needs to be empty!
        """
