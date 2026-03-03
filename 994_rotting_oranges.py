class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_cnt = 0
        rotten = deque()

        # # Time - O(N), Each element was visited once
        for r in range(rows):
            for c in range(cols):
                # Space: O(N), each cell is added/popped within queue at most once
                if grid[r][c] == 2: 
                    # add the rotten orange to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # initial count of fresh oranges
                    fresh_cnt += 1

        min_passed = 0
        
        # Time - O(N)
        # if there are oranges in the queue and there are still fresh oranges, keep looking
        while rotten and fresh_cnt > 0:
            min_passed += 1

            # process rotten oranges in level by level - Multi source BFS
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all adjacent cells - 4 neighbors (constant work).
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    
                    # update the fresh orange count as we mark the newly rotten oranges
                    fresh_cnt -= 1
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2

                    # add the current rotten to the queue
                    rotten.append((xx, yy))
        
        if fresh_cnt == 0:
            return min_passed
        else:
            return -1
