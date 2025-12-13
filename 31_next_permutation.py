class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        We notice that for any given sequence that is in descending order,
        no next larger permutation is possible. e.g: 321

        Time: O(N), Space: O(1)
        """
        # First we find pivot in the num such that it start to decrease
        # Example: 432531 => we want to capture 5
        i = len(nums)-1
        while i-1 >= 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        # either there was no next num and we reached at the end as example 321
        if i == 0:
            nums.reverse() # in-place reversal
            return
        # we found the pivot
        else:
            pivot=i-1
            # find a num that is great than this one we can swap with
            # ex: 2531, this can be increased, the smallest num that can be swapped is 3
            swapind = len(nums)-1
            while nums[swapind] <= nums[pivot]:
                swapind -= 1
            # we've found the swap index
            nums[swapind], nums[pivot] = nums[pivot], nums[swapind]
        
        # print("we should have: 43|3521")
        # print(nums)
        # now we want to minimize whatever is after the pivot index by just reversing 43|3|521
        end = len(nums)-1
        start = pivot+1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        # we should end up with 43|3|125
        return