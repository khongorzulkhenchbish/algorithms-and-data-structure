class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ''' ramp = subarr. find max subarr where start < end number.
        - arr elements: positive [0, 5*10^4], not sorted
        - if everything is strictly decreasing, return 0
        - max possible value is the arr length itself. if it is either [1,...,1 or x] where x>1 
        - arr len = [2, 5*10^4]

        [1,1], [2,1] => 0, 0
        [1,3] => (1,3) => 2
        [1,5,3] => 2, whatever can be in the middle
        2 interesting cases:
        [10,6,7,11] => 4
        [10,6,7,9] => 3

        Brute Force:
        - for every fixed left elem, find its right far reach, update max len => time: O(n^2)
        Q1: can I find a future number that is farthest than me? 
            -> right pointer iterates from the end, stops once it finds the first.
            [10,9,(6,7,8,9),3,1]
            fix=10 find nothing
            fix=9. find nothing
            fix=6, find 9, max_width=4
            fix=7, no need to iterate from 9 to left, instead iteration range
            n ... last_index of 9, which is just to check between (3,1) now
            => time: best: [1,2,3,,5] - O(N), worst: [5,4,..1] - O(n^2)
        Q2: can this be optimized with data structure?
            [10,9,(6,7,8,9),3,1] => let's determine from which indexes the subarr could start.
            fix=10, 9, 6, but not 7, not 8, not 9, not 3.
            when the arr elem increases, if we had i<j, such that num[i]<num[j], then num[j] as starting point
            will only shrink the subarray. Therefore, subarr can be started from only decreasing indexes.
            => Monotonic stack for the indexes. Space: O(N), Time: O(2N)

        Google Alternative: Find maximum length of a substring of a string with first character
        lexicographically smaller than its last charachter. Assume string length 10^5 char long,
        assume 26 small case english letters in string solve it in linear time.

        Solution: direct comparison of strings: s[i] < stack[-1], 'a' < 'b', max_length=(j-i+1)
        Space: O(26) Why? Because it's a strictly decreasing stack. Once you hit 'a', you can't add anything else.
        '''
        if not nums or len(nums) < 2:
            return 0

        max_width = 0
        dec_stack = [0]

        # Phase 1: Build a strictly decreasing stack of candidate starting indices
        for i in range(1, len(nums)):
            # Only add if this is the smallest value seen so far
            # [9, 8, 100, 99, 4, 4, 4, 4, 4, 4, 5] => [9,8,4] => indexes = [0,1,4] so we will capture [4,4,,5]
            # Optimization: When building the stack, skip duplicate values,
            # because dec_stack[-1] will bring longer subarr, so skip adding current i
            if nums[i] < nums[dec_stack[-1]]:
                dec_stack.append(i)
        
        # Phase 2: Traverse backwards to find the maximum width: furthest possible j it could ever reach
        # Now the stack is strictly decreasing: e.g., [9, 8, 1, 0]
        # No 'barriers' like '4' will block our j from reaching the '0'
        # Each index is pushed and popped once
        for j in range(len(nums) - 1, -1, -1):
            # When the values are equal, it counts!
            # # While the current end 'j' can form a ramp with the 'start'
            while dec_stack and nums[dec_stack[-1]] <= nums[j]:
                start_ind = dec_stack.pop()
                max_width = max(max_width, j - start_ind)
        
        return max_width

        # ex 1: [6,0,8,2,1,5], dec_stack = [0,1,3,4]
        # j = 5, 4, 3, 2, 1, 0
        # start_ind = 4, dec_stack = [0,1,3] => [0,1] => [0] => []
        # max_width = 0, 1, 2, 4, 2, 1 => 4

        # ex 2: [3,3], dec_stack = [0]
        # j = 1, 0
        # start_ind = 0, dec_stack = [], 
        # max_width = 0, 1 => 1