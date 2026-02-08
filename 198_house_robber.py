class Solution:
    def rob(self, nums: List[int]) -> int:
        ''' The idea is to understand that at every step, you either rob cur house or not.
        If you won't rob cur house, you should rob the prev house and count that instead.
        At each step, we should calculate the max amount we could collect.
        Time: O(N), Space: 0(1)
        '''
        if len(nums) == 1:
            return nums[0]
        
        # [prev2, prev1, nums[i], nums[i+1], ...]
        prev2 = nums[0]
        prev1 = max(nums[1], prev2) # [2,1,1,2] at [2,(1)|1,2], the max arr should be [2,(2)|3,4]
        currMax = prev1

        for i in range(2, len(nums)):
            currMax = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = currMax # not nums[i] because we are saving the result array values here already.
        
        return currMax

        ''' The intuition on example:
        DP without memory
        [2 | 0, 3, 5, 1]
        max until 2 is 2 => maxGold=[2,0,0,0,0]

        [2, 0 | 3, 5, 1]
        max until 0: we either take 2 or just 0, so max(nums[0], nums1) => maxGold=[2,2,0,0,0]

        [2, 0, 3 | 5, 1]
        max until 3: we either take 3 (plus we add max until 2) or we ignore 3 and take max until 0
        try both and set max until 3: max(prev2 + curr, prev1)=max(2+3, 2) => maxGold=[2,2,5,0,0]

        [2, 0, 3, 5 | 1]
        max until 5: we either take 5 (plus we add max until 0) or we ignore 5 and take max until 3
        try both and set max until 5: max(prev2 + curr, prev1)=max(2+5, 5) => maxGold=[2,2,5,7,0]

        [2, 0, 3, 5, 1]
        max until 1: we either take 1 (plus we add max until 3) or we ignore 1 and take max until 5
        try both and set max until 1: max(prev2 + curr, prev1)=max(5+1, 7) => maxGold=[2,2,5,7,7]

        return the last max 7
        '''

        # Recursive approach: Time: O(2^N) TLE, Space: O(N)
        # n = len(nums)

        # def helper(i):
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0], nums[1])
            
        #     return max(helper(i-2)+nums[i], helper(i-1))
        
        # return helper(n-1) # call on the last elem
        