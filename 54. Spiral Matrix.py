class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Algorithm :
        # 1. Define Boundaries:
        #   - top: Tracks the topmost unvisited row.
        #   - bottom: Tracks the bottom-most unvisited row.
        #   - left: Tracks the leftmost unvisited column.
        #   - right: Tracks the rightmost unvisited column.

        # 2. Use a loop to simulate the spiral traversal:
        #   - Traverse the top row from left -> right then increment top.
        #   - Traverse the right column from top to bottom then decrement right.
        #   - Traverse the bottom row from left <- right (if still valid) and decrement bottom.
        #   - Traverse the left column from bottom to top (if still valid) and increment left.
        
        # Append elements to the result list during traversal.

        # Complexity Analysis :
        # Time Complexity: O (m × n). Each element of the matrix is visited once.
        # Space Complexity: O(1) additional space. The result array O( m×n) is required for output.

        result = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        while top <= bottom and left <= right:
            # Traverse top row
            for j in range(left, right+1):
                result.append(matrix[top][j])
            top += 1

            # Traverse right column
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom row (if valid)
            if top <= bottom:
                for j in range(right, left-1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse left column (if valid)
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result