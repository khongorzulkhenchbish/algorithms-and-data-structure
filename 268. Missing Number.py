class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Intuitive approach input: nums=[3,0,1]
        we know the range is 0,1,2,3 and there are 4 numbers in total,
        but the given input only has 3 total numbers: 0, 1, 3.

        suppose sum = 0 + 1 + 2 + 3 = 6
        current sum = 0 + 1 + 3 = 4
        6 - 4 = 2

        2 is the missing number in [0, 1, 3]
        No sorting or hash map is required in this approach.
        Time: O(N), Space: O(1)
        """

        maxn = max(nums)
        maxsum = maxn * (maxn+1) // 2   # calc sum if no number was missing
        diff = maxsum-sum(nums)
        
        if diff == 0:           # edge case: when [0,1] is given, we should return 2
            if min(nums) == 0:  # edge case: when [1,2] is given, we should return 0 if it was in the arr
                return maxn + 1 
        return diff

        # Naive approach
        # sorted_nums = sorted(nums)

        # for ind, val in enumerate(sorted_nums):
        #     # print(ind, val)
        #     if ind != val:
        #         return ind
            
        # return len(nums)
