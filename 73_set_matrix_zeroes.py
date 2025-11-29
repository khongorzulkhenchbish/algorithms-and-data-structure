class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #List keep track of which rows/columns are 0
        R = set()
        C = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    R.add(i)
                    C.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in R or j in C:    # if current item is in the row or column that contains 0, then set it to 0
                    matrix[i][j]=0
                
        return matrix
        # Space: O(m+n), Time: O(2*m*n)
