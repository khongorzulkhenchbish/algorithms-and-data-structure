class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # The intuition is hard to come up with.
        # The math property holds that if we find two remainder  from the pefix sums such that
        # they are not adjacent, then that means the elements between that are subarray with
        # its sum divisible by k.

        # Time: O(N), iterate each num once, add/lookup in the hashmap is O(1)
        # Space: O(N), we could end up storing every elements+indexes when there is no such subarray.
        if len(nums) <= 1:
            return False
        
        # setting this prevents from the first number itself to be considered as subarray
        # as it has length 1
        remainder = { 0: -1 }    # remainder: location
        prefixsum = 0

        for i, num in enumerate(nums):
            prefixsum += num
            curr_rem = prefixsum % k

            # [23,2,4,6,7] => prefixSum = [23,25,29,35,42]
            # remArr = {0:-1, 5:0, 1:1, 5:2, 5:3, 0:4}
            # we have subarray between nums[0:2], nums[0:3], also nums[0:5]
            
            # subproblem: two sum
            if curr_rem in remainder:
                # length of the subarray should be more than 2
                if i - remainder[curr_rem] >= 2:
                    return True
            else:
                remainder[curr_rem]=i
        
        return False

        # Brute force: O(n^2) TLE 92/105
        # if len(nums) <= 1:
        #     return False
        
        # for i in range(len(nums)):
        #     curr_sum = nums[i]
        #     for j in range(i+1, len(nums)):
        #         curr_sum += nums[j]

        #         if curr_sum % k == 0:
        #             return True
        
        # return False