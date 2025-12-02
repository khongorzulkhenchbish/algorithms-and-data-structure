# sortedcontainers library provides SortedList, SortedDict and SortedSet data types
# It maintains items in sorted order as new elements are added or removed.
from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """
        Time: O(N*logN)
        Space: O(N)

        min_abs_diff(nums[i], nums[j]) where |i - j| >= x

        Intuition:
        For every j, there are nums[0:j-x] elements that has possible min diff.
        This sublist can have larger size for calculate diff between each elem and nums[j].
        We rather use Binary Search to optimize to find the indexes such that
        condition holds and gives us the min_diff (nums[left] <= nums[j] <= nums[right])
        """
        sorted_list = SortedList()
        min_diff = float('INF')     # max num possible

        for j in range(x, len(nums)): # time: O(N)
            # add the previous elems in x distance one by one to the set
            sorted_list.add(nums[j-x])

            # Find the position where current element would be inserted
            # in the sorted list (binary search) - time: O(logN)
            # returns 1 for bisect_left([3,4], 4) tells that new 4 should be inserted on the left.
            insert_pos = bisect_left(sorted_list, nums[j])

            # current elem - left side elem
            if insert_pos < len(sorted_list):
                min_diff = min(min_diff, sorted_list[insert_pos] - nums[j])

            # right side elem - current elem
            if insert_pos > 0:
                min_diff = min(min_diff, nums[j] - sorted_list[insert_pos-1])
        
        return min_diff
        """
        nums = [4,3,2,4] x = 2
        j = 2
        sorted_list=[(2)4] => min_diff = 4-2 => 2
        j = 3
        sorted_list=[3, 4, (4)] => bisect => 2 => min_diff => (2, 4-4) => 0
        """