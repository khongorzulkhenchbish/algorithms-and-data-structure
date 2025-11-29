class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        core idea: instead of searching paths, search for the answer
        range of t value: [0, n*n-1]. e.g: 5x5 matrix, t value is between [0, 24]
        """
        def dfs(i, j, t, visited):
            if i == n-1 and j == n-1 and grid[i][j] <= t:
                # reached the end cell
                return True

            if i < 0 or j < 0 or i >= n or j >= n or (i,j) in visited or grid[i][j] > t:
                return False
            
            # mark as visited
            visited.add((i, j))

            return (
                    dfs(i+1, j, t, visited) or
                    dfs(i-1, j, t, visited) or
                    dfs(i, j+1, t, visited) or
                    dfs(i, j-1, t, visited)
                    )
            

        # set binary search range - log(n^2)
        n = len(grid)
        left = 0
        right = n*n-1
        print(left, right, n)
        
        while left < right:
            # mid is the guess for the minimum time
            mid = left + (right - left) // 2

            # simple path finding algorithm O(n^2) to check 
            # if from cell 0,0 reaching n-1,n-1 is possible where grid[i][j] <= mid
            pathExists = dfs(0, 0, mid, set())

            if pathExists:
                right = mid # try the lower half for shorter time
            else:
                left = mid+1  # try to higher half for longer time
        
        # left == right which is the answer
        return left