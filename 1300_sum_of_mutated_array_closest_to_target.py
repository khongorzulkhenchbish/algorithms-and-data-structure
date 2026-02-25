import bisect

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        ''' arr = [4,9,3] target = 10
        x = 3 then we can modify only nums higher than 3 => arr = [3,3,3] = diff sum = 10-9 = 1
        x = 4 then we can modify only nums higher than 4 => arr = [4,4,3] = diff sum = 11-10 = 1 => tie => min=3
        x = 9 there is no higher number than 9, arr = [4,9,3] = diff sum = 16-10 = 6

        what if target = 12 ?
        x = 3, arr = [3,3,3] = 9-7=2
        x = 4, arr = [4,4,3] = 11-7=4
        x = 5, arr = [4,5,3] = 12-12=0 => min = 5
        x = 9, arr = [4,9,3] = 16-12=4

        1. sort - nums will be ordered [3,4,9]
        2. binary search range: low = 0, high = max(arr)

        The Sum of the mutated array is monotonic (as x increases, the sum increases).
        '''
        # Optimal approach: O(N log N + log K*log N)
        arr.sort() # All elements from index 0 to k-1 remain unchanged. Their sum is prefix_sum[k]
        n = len(arr)
        
        # Precompute prefix sums for O(1) range sum queries
        # prefix[i] = sum of arr[0...i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
            
        def get_mutated_sum(x):
            # Find the first index where arr[i] >= x
            idx = bisect.bisect_left(arr, x)
            # Sum = (elements < x) + (remaining elements replaced by x)
            return prefix[idx] + (n - idx) * x

        # Binary search for the value of x
        low, high = 0, arr[-1]
        while low < high:
            mid = (low + high) // 2
            if get_mutated_sum(mid) < target:
                low = mid + 1
            else:
                high = mid
        
        # Candidate 1: 'low' is the first value where sum >= target
        # Candidate 2: 'low - 1' is the last value where sum < target
        val1 = low
        val2 = low - 1
        
        sum1 = get_mutated_sum(val1)
        sum2 = get_mutated_sum(val2)
        
        # Tie-breaker: choose the smaller value if differences are equal
        if abs(sum2 - target) <= abs(sum1 - target):
            return val2
        return val1

        # Approach 1: O(N log K)
        # def calculate_mutated_sum(x):
        #     total = 0
        #     for num in arr:
        #         # If num > x, it becomes x. Otherwise, it stays num.
        #         total += min(num, x)
        #     return total

        # # Search range is from 0 to the maximum element in the array
        # low = 0
        # high = max(arr)
        
        # # Binary search for the value that gets us closest to the target
        # while low < high:
        #     mid = (low + high) // 2
        #     if calculate_mutated_sum(mid) < target:
        #         low = mid + 1
        #     else:
        #         high = mid
        
        # # After the loop, 'low' is the first value where sum >= target.
        # # We must check if 'low' or 'low - 1' is actually closer to the target.
        # sum_at_low = calculate_mutated_sum(low)
        # sum_at_prev = calculate_mutated_sum(low - 1)
        
        # if abs(target - sum_at_prev) <= abs(target - sum_at_low):
        #     return low - 1
        # return low