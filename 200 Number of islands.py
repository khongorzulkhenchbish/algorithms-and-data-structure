class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands=0 
        for i in range(len(grid)): #rows 
            for j in range(len(grid[0])): #cols
                if grid[i][j]=='1': #if we found land
                    self.dfs(grid,i,j) #
                    islands+=1
                    
        return islands
        
    def dfs(self, grid, x, y):
        grid[x][y]='0'
        
        coords=[(x,y), (x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        for point in coords:
            nx=point[0]
            ny=point[1]
            if(nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0])):
                if(grid[nx][ny]=='1'):
                    self.dfs(grid, nx, ny)
        return
          

