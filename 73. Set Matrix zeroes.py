class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #List keep track of which columns are 0
        colSet = set()
        
        
        #List keep track of which rows are 0
        rowSet = set()
        
        # Iterate through matrix and find zeroes
        for row in range(len(matrix)): #Row index
            for col in range(len(matrix[0])): #Column index
                if matrix[row][col] == 0: #Check matrix value is 0
                    colSet.add(col) #Add column number to set
                    rowSet.add(row) #Add row number to set
    
        
        #Change column numbers to 0
        for colIndex in colSet: 
            for row in range(len(matrix)): 
                matrix[row][colIndex] = 0
        
        #Change rows of matrix
        for rowIndex in rowSet: 
            matrix[rowIndex] = [0] * len(matrix[rowIndex])
            
        print(matrix)
