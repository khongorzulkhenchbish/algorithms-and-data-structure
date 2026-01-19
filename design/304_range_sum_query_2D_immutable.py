class NumMatrix:
    """ Let's think on 1D array.
    Prefix sum over the row: [3 (0 1 4) 2] => [(3), 3, 4, (8), 10] = 8 - 3 => (0 1 4) => 5
    Prefix sum over the col will be the same. Mind that there will be overlap of sum[row-1][col1].

    After considering this, we will have the prefix sum of 2D array.
    Then we will subtract the top right and left bottom sub rectangle sums from the given cell,
    and here the previous diagonal sum will be subtracted twice as it is included in above two,
    so we add it back.

    Time: O(n) for init, O(1) for sumRegion. Space: O(1) as we modified the original array.
    
    NOTE: If we add padding, this would be faster than <if> which slows down the speed.
    Create a padded matrix of zeros (R+1 x C+1)
    This removes the need for all those "if row-1 >= 0" checks
    self.ps = [[0] * (C + 1) for _ in range(R + 1)]
    """
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # assuming we can modify the original matrix
        for row in range(rows):
            for col in range(cols):
                left = 0
                if row-1 >= 0:
                    left = matrix[row-1][col]
                
                top = 0
                if col-1 >= 0:
                    top = matrix[row][col-1]

                prev_diag = 0
                if col-1 >= 0 and row - 1 >= 0:
                    prev_diag = matrix[row-1][col-1]
                
                # add both to current cell, remove the overlapping cell sum
                matrix[row][col] += (left + top - prev_diag)
        
        # prefix sum matrix
        # for row in matrix:
        #     print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        col_sum = 0
        if col1-1 >= 0:     # left bottom
            col_sum = self.matrix[row2][col1-1]
        
        row_sum = 0
        if row1-1 >= 0:     # right top
            row_sum = self.matrix[row1-1][col2]
        
        prev_diag_sum = 0
        if row1-1 >= 0 and col1-1 >= 0:
            prev_diag_sum = self.matrix[row1-1][col1-1]
        
        return self.matrix[row2][col2] - row_sum - col_sum + prev_diag_sum

    # Approach 1: Uses the prefix sum across the row. Time complexity for sumRegion: O(row2-row1)
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     for row in range(rows):
    #         col = 0
    #         prev_sum = matrix[row][col]
    #         for col in range(1, cols):
    #             matrix[row][col] += prev_sum
    #             prev_sum = matrix[row][col]
    #         print(matrix[row])



    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     # [2, 1, 4, 3]
    #     total_sum = 0

    #     for row in range(row1, row2+1):
    #         if col1-1 < 0:
    #             row_sum = self.matrix[row][col2]
    #         else:
    #             row_sum = self.matrix[row][col2] - self.matrix[row][col1-1]
    #         total_sum += row_sum

    #     return total_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)