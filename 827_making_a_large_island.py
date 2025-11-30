class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Cases
        00          11     
        00 => 1     11 => 4

        00100
        11011
        00100 => 7
        """
        # Time: O(2N) for visiting twice, Space: O(N) in the worst case we have chessboard like structure to store the unique islands 
        N = len(grid)
        def out_of_bounds(r, c):
            return (r < 0 or c < 0 or r == N or c == N)

        def dfs_area(r, c, label):
            # if it has been visited already we will skip
            if out_of_bounds(r, c) or grid[r][c] == 0 or grid[r][c] == label:
                return 0
            # else:
            
            # each cell with have unique label assigned
            grid[r][c] = label
            # start counting the island
            size = 1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            # calculate the sub matrix sum
            for x,y in directions:
                size += dfs_area(r+x, c+y, label)
            return size

        label = 2
        areas = {}
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 1. Precompute the areas
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    # dfs should return the total num of islands
                    areas[label] = dfs_area(r, c, label)
                    # change island id for the next island
                    label += 1

        # 2. Flip zeros, while calculating possible max num of islands after connecting
        maxIsland = 0 if not areas else max(areas.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    currSize = 1 # flipped zero itself
                    visit = set()
                    # try to connect
                    for x,y in directions:
                        dr = r + x
                        dc = c + y
                        if not out_of_bounds(dr, dc) and grid[dr][dc] not in visit and grid[dr][dc] != 0:
                            currSize += areas[grid[dr][dc]] # increment those that are not zero
                            visit.add(grid[dr][dc])
                    
                    maxIsland = max(maxIsland, currSize)

        return maxIsland
        """
        dry run
        00100       label = 2, 3, 4, 5              00200
        11011       areas = {2:1, 3:2, 4:2, 5:1}    33044
        00100                                 =>    00500
        then
        visited = (3)           => (2,3)                       => 3 ... => (3,2,4,5)
        currSize = areas[3] = 2 => areas[2] + areas[3] = 1 + 2 => 3 ... => areas[2] + areas[3] + areas[4] + areas[5] = 1+2+2+1 => 6+1(0 inc)
        maxIsland = (0,2) => 2  => (2, 3)                      => 3 ... => maxIsland (3+1, 6+1) => 7
        """