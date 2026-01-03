class Solution:
    def minLength(self, nums: List[int], k: int) -> int:\
        # Time: O(n), Space: O(n)
        # NOTE: add the duplicate nums in the subarray sum just once!!! 
        freq = Counter() # hashmap "num":frequency
        left, right, minlen = 0, 0, inf
        
        subarray_sum = 0
        for right, cur_num in enumerate(nums):
            freq[cur_num] += 1
            if freq[cur_num] == 1: # only extend the array when the subarray has unique elems
                subarray_sum += cur_num
            
            # shrink from the left as much as we can
            while subarray_sum >= k:
                # update with the shorter length
                minlen = min(minlen, right-left+1)
                # we don't have keep the left most because even adding the right next elem,
                # the sum will be higher than k anyway
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0: # repeated elem
                    subarray_sum -= nums[left]
                
                left += 1

        print(freq)
        return minlen if minlen < inf else -1

        """ Example 1. nums = [2,2,3,1] k = 4
        freq = {2:2, 3:1} => {2:1,3:1} => {2:1, 3:0, 1:1}
        subarray_sum = 0, 2, 5, 2, 3
        right = 0, 1, 2, 3, 4
        cur_num = 2, 2
        left = 0, 1, 2
        minlen = inf, 3, 2, => 2

        Example 2. nums = [1,2,3,3,4], k = 8
        freq = {1:1, 2:1, 3:2, 4:1} => {1:0, 2:0, 3:2, 4:1}
        subarray_sum = 0, 1, 3, 6, 10, 9, 7
        right = 0, 1, 2, 3, 4
        left = 0, 1, 2
        minlen = inf, 5, 4
        
        """
        