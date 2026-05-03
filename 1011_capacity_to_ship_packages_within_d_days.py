from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            days_used = 0
            current_load = 0

            # can we deliver mid capacity?
            for weight in weights:
                current_load += weight

                if current_load == cap:
                    days_used += 1
                    current_load = 0

                elif current_load > cap:
                    days_used += 1
                    current_load = weight
            
            if current_load > 0:
                days_used += 1
            
            return days_used <= days


        """
        n amount of weights, not sorted but order is important,
        must be shipped in given days, find min capacity
        Time: O(N*logM) where M is the sum(weights)-max(weights)+1
        Space: O(1)
        """
        left = max(weights) # the min cap we can accept
        right = sum(weights) # the max cap, if the days=1

        while left <= right:
            mid = (left + right) // 2

            if can_ship(mid):
                left = min(left, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        """
        1. weights = [10,20,30], days = 1 expected 60, all in one day
        2. weights = [3, 2, 2, 4, 1, 4], days = 6 expected 4, [ 3 | 2 | 2 | 4 | 1 | 4 ]
        3. weights = [1, 2, 3, 1, 1], days = 4 expected 3, [1, 2 | 3 | 1 | 1]
        """