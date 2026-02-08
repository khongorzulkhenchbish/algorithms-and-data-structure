class Solution:
    def mySqrt(self, x: int) -> int:
        # Time: O(logN), Space: O(1)
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2

            power = mid*mid
            # Edge condition: when mid=2, 4 <= 8 <= 9, we should return 2 as 3^2 will be way higher
            if power <= x and x < (mid+1)*(mid+1):
                return mid
            elif x < power:
                right = mid - 1
            else: # power < x
                left = mid + 1
        
        # 0, 8 => 0, 3 => 2, 3
        # 4 => 16   1 => 1    2 => 4
