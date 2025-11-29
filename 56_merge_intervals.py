'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

class Solution:
    def merge(self, intervals):
        
        # Sort intervals in increasing order of start times
        intervals.sort(key = lambda x: x[0])
        
        # Return value will be a list of lists (list of interval lists)
        merged = []
        
        # Iterate all intervals
        for interval in intervals:
            
            # start by adding the first interval to the list 
            # (if the list of intervals is empty (not merged) then add the 1st interval)
            
            # or, if the recently added/last/previous interval from the list 
            # can not be merged with "interval", 
            # then add "interval" to the list
            
            # to check if 2 intervals can be merged, 
            # we check if the recently added interval's "end time"
            # is less than "interval's" "start time" 
            # recentlyAddedInterval[1] < interval[0]
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            
            # if the recently added/last/previous interval from the list 
            # can be merged with "interval", 
            # then change the end time of the recently added/last/previous interval
            # to be the latest end time between the previous interval and "interval"
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
    # Time complexity : O(n log n)
    # The runtime is dominated by the O(n log n) complexity of sorting.
    
    # Space complexity : O(log n) or O(n)
    # Sorting takes O(log n) space in memory
    # But if the sorting is in-place, then we only need constant space
    # and we only allocate linear space to store a copy of intervals, to sort
    
'''
Runtime: 88 ms, faster than 44.22% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 5.59% of Python3 online submissions for Merge Intervals.
'''