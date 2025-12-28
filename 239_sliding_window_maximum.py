class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_arr = []
        window = collections.deque() # store index
        left = right = 0

        while right < len(nums):
            # make sure window[0] has the largest of the sub window
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            # at every step we expand the window whatever happens
            window.append(right)

            # remove the left val from window -> still don't understand
            if left > window[0]:
                window.popleft()
            
            # when the window size exceeds k, we move the left pointer by 1 to the right
            if right-left+1 >= k:
                max_arr.append(nums[window[0]]) # window[0] stores the current window max val
                left += 1
            
            # at every step we expend the window by 1
            right += 1
        
        return max_arr
        """ Example:
        nums = [1,3,-1,-3,5,3,6,7], k = 3
        max_arr = [3, 3, 5, 5, 6, 7]
        window = [0] => pop & add => [1, 2, 3] => pop & add = [4, 5] => pop & add = [6] => pop & add = [7]
        left = 0, 1, 2, 3, 4, 5, 7
        right = 0, 1, 2, 3, 4, 5, 6, 7, 8

        Example 2:
        nums = [1,-1]   k = 1
        max_arr = []
        window = [0, 1] => popleft = [1]
        left = 0, 1
        right = 0, 1
        """
