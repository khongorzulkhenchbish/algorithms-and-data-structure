class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # By creating a new array (flattening), O(N*M) time and O(N*M) space
        # Optimal - Time: O(log N*M), Space: O(1)
        # For a 1000x1000 matrix, you're comparing ~20 operations vs 1,000,000 operations.

        if not matrix or not matrix[0]: # matrix = [[]]
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Virtual flattening mapping
            num = matrix[mid // cols][mid % cols]
            # Imagine movie theatre. The row index changes only after you have filled
            # an entire column's worth of seats. Therefore:
            # Row = index // cols 
            # Column = index % cols
            
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False