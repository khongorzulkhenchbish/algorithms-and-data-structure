class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Space: O(1)     Time: O(N*N) but still linear
        Do not return anything, modify matrix in-place instead.
        5  1  9  11
        2  4  8  10
        13 3  6  7 
        15 14 12 16
        """
        # Following algorithm works only for (N x N) equal dimensional matrix

        # first transpose
        for i in range(len(matrix)): # rows [0, 1, 2, 3]
            for j in range(i, len(matrix[0])): # [0,1,2,3, 1,2,3, 2,3, 3]
                # starting from i ensures to modify only swapping that rows elements
                # so when we move to the new row, we won't encounter reverse swapping
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                """
                5  2  13  15
                1  4  3  14
                9  8  6  12
                11 10 7  16
                """

        N = len(matrix[0])
        # swap horizontally symmetrical
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2): # avoids double swapping, skips the middle col
                matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
                """
                [a, b, c, d, e] => swapIndex(0, 5-1-0), swapIndex(1, 5-1-1), j => 2 == N/2 stops
                15 13 2  5      i = [0, 1, 2, 3]
                14 3  4  1      j = [0, 1]
                12 6  8  9      N = 4   swapIndex(j, N-j-1)
                16 7  10 11
                => Rotation Completed!
                """
        