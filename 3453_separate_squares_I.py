class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        ''' As the line y moves up, the area below will always increases. Same otherways.
        Guess a y, calculate the area below, and adjust the y such that (below_area = total_area/2)
        Binary search: y's val is always between min(y1, y2) and max(y1+l1, y2+l2)
        so we could narrow down the correct y value.

        Time: O(Nlog(Range/Precision))
        '''
        # 1. Find the total area and the vertical bounds
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            
        target = total_area / 2

        # 2. Helper function to calculate area below line y = k
        def get_area_below(k):
            area = 0
            # sum all the subareas under current k/y line.
            for x, y, l in squares:
                if k <= y:
                    continue # square is above line k, no area to catch
                elif k >= y + l:
                    area += l * l # square is under the line k, whole square to catch
                else:
                    # Line k is inside the square (partially), capture the diff of heights
                    area += l * (k - y)
            return area
        
        # 3. Binary search on the y-coordinate
        low, high = min_y, max_y
        # 100 iterations provide more than enough precision for 10^-5
        for _ in range(100):
            mid = (low + high) / 2  # mid is the guessed line k
            if get_area_below(mid) < target:
                low = mid
            else: # if area is higher or equal, we still need to decrement k as much as possible.
                high = mid
                
        return low