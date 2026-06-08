class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        # Because the player 1 only moves down/right and player 2 moves up/left, their
        # paths only meets vertically or horizontally in one or more cells.
        # Therefore the problem boils down to finding the maximum contiguous subarray sum
        # in any single row or column.
        # Kadane's algorithm, does this within linear time: O(rows x cols) is linear
        rows = len(grid)
        cols = len(grid[0])

        def is_interior(row, col):
            return 0 < row < rows-1 and 0 < col < cols-1
        
        # best valid segment seen anywhere so far
        max_sum = float('-inf')

        # iterate row by row
        for row in range(rows):
            # best sum of a contiguous segment ending at the current cell
            prefix_sum = grid[row][0]
            # for each row, iterate col by col, starting from the second column
            for col in range(1, cols):
                extend = prefix_sum + grid[row][col]
                max_sum = max(max_sum, extend)
                # if the shared cell is exactly one, then the cell must be
                # strictly inside the grid, not on the edges.
                # so only compare with the current cell
                if is_interior(row, col):
                    max_sum = max(max_sum, grid[row][col])
                # do we want to start new sum from curr elem or not.
                prefix_sum = max(grid[row][col], extend)
        
        for col in range(cols):
            prefix_sum = grid[0][col]
            for row in range(1, rows):
                extend = prefix_sum + grid[row][col]
                max_sum = max(max_sum, extend)
                if is_interior(row, col):
                    max_sum = max(max_sum, grid[row][col])
                prefix_sum = max(grid[row][col], extend)
        
        return max_sum