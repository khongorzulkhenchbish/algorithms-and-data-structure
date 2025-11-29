class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        brute force: left and right pointer, where left is fixed and right one extends always.
        It goes until we run out of k and we encounter 0.

        optimal approach: also sliding window, but "What is the longest subarray that has at most K zeroes?"
        we can extend the right until we have k zeroes. Then we can shrink left until we find 0 => left+=1.
        Time: O(N), in the worst case, we might end up visiting every elem of the arr twice by left anf right pointers
        Space: O(1), no extra space
        """
        left = right = 0
        zeroes = 0
        maxlen = 0

        for right in range(len(nums)):
            # if we can still add zeroes
            if nums[right] == 0:
                zeroes += 1

            # continue until there is no 0s
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -=1
                left += 1

            # update the maxlen
            maxlen = max(maxlen, right-left+1)
        
        return maxlen
        """
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        zeroes = 1
        maxlen = 6
        nums[left] = nums[5] = 0
        nums[right] = nums[10] = 0
        """