# DFS
class Solution(object):
    def numIslands(self, grid):
        def paint(row, col):
            grid[row][col] = '0'

            nbs = [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]
            for nr, nc in nbs:
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    if grid[nr][nc] == '1':
                        paint(nr, nc)
            return

        # Constraints:
        # Is it allowed to mutate the grid in-place?
        # 1 <= rows, cols <= 300, for the largest grid we store 90'000 cells
        # Time: O(R * C) each cell visited once, the recursive call won't add extra asymptotic time
        # Space: O(R * C) in-place modification -> aux space is recursion stack worst-case O(R*C)
        counter = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows): # rows 
            for col in range(cols): # cols
                if grid[row][col] == '1': #if we found land
                    paint(row,col)
                    counter += 1    
        return counter


# BFS - Excellent for avoiding recursion depth issues.
from collections import deque

class Solution(object):
    def numIslands(self, grid):
        def bfs(row, col):
            q = deque()
            q.append((row, col)) # add as tuple

            while q:
                r, c = q.popleft()
                directions = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < cols and
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                            q.append((nr, nc))
                            visited.add((nr, nc))

        # time: O(R*C) each cell visited just once
        # Aux space: O(R*C) worst case (visited + queue frontier)
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        for row in range(rows): 
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands
    
    '''
    
      ["0","0","0","1","0"],   number of island = 1
      ["0","1","1","1","0"],
      ["0","0","0","0","0"],   number of island = 2
      ["0","0","0","0","0"]    number of island = 3
    
    '''
    
          

