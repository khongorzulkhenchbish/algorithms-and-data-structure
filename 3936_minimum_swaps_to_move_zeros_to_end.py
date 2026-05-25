class Solution:
    # should we keep the order of non-zeros? - doesn't matter
    # what counts as one operation? - one swap, one operation, any two distinct indices
    # if zeros are already in the last k slots, answer is 0

    # Let k = count(0). Any zero in nums[0:n-k] is misplaced.
    # Each swap can move exactly one such zero into the suffix.
    # min_swap = # of zeros in prefix nums[0:n-k]
    def minimumSwaps(self, nums: list[int]) -> int:
        # time: O(N) for count
        zero_count = nums.count(0)
        n = len(nums)

        # space: O(1) excluding the array for n <= 100
        # return nums[0:n-zero_count].count(0)

        # space: O(1) for n >= 100, the previous one creates auxilary array with O(N)
        misplaced_zeros = 0

        for i in range(n-zero_count):
            if nums[i] == 0:
                misplaced_zeros += 1
        
        return misplaced_zeros
    
    # 1. no zeros, [1,2,3] -> 0
    # 2. all zeros, [0,0,0] -> 0
    # 3. single zero, [0,1,2] -> 1
    # 4. all valid, [1,2,0] -> 0