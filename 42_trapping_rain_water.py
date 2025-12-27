class Solution:
    def trap(self, height: List[int]) -> int:
        """ The idea is to collect the left and right side max values for each cell,
        the min of these two means the max height of water that can be trapped.
        Next we have to decrement the current height so we will get the possible
        amount of water that can be trapped.
        Time: O(N), Space: O(N).
        Example: height = [4,2,0,3,2,5]
        """
        if len(height) == 0:
            return 0

        n = len(height)
        leftMax = [0 for i in range(n)]
        rightMax = [0 for i in range(n)]

        leftMax[0] = 0
        for i in range(1, n):
            leftMax[i] = max(height[i-1], leftMax[i-1])
        # height =  [4, 2, 0, 3, 2, 5]
        # leftmax = [0, 4, 4, 4, 4, 4]

        rightMax[n-1] = 0
        for i in range(n-2, 0, -1):
            rightMax[i] = max(height[i+1], rightMax[i+1])
        # height =   [4, 2, 0, 3, 2, 5]
        # rightmax = [0, 5, 5, 5, 5, 0]

        total = 0
        for i in range(1, n-1):
            currsum = min(leftMax[i], rightMax[i]) - height[i]
            if currsum > 0:
                total += min(leftMax[i], rightMax[i]) - height[i]
        # here is the main logic
        # curr_water = min(leftmax, rightmax) - curr_height
        # height =   [4, 2, 0, 3, 2, 5]
        # leftmax =  [0, 4, 4, 4, 4, 4]
        # rightmax = [0, 5, 5, 5, 5, 0]
        # curr_wat = [-, 2, 4, 1, 2, -] => 9

        return total