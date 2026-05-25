class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # time: O(R*C) 
        def countArea(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            # grid[r][c] is 1
            count = 1
            # mark as visited
            grid[r][c] = 0

            count += countArea(r+1,c)
            count += countArea(r-1,c)
            count += countArea(r,c+1)
            count += countArea(r,c-1)

            return count


        rows = len(grid)
        cols = len(grid[0])

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = countArea(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea
        """
        0000 => area = countArea(0,2) => count = 1 + countArea(1,2) => 1 + 1 + 
        1000    => countArea(1,2) => 1 + 1 + countArea(2,2) =>
        1000 => 4  => 1 + 1 + countArea(2,2) => 1 + 1 + 1 + countArea(2,3) =>  1 + 1 + 1 + 1 + 0 => 4
        stop if out of boounds.
        """