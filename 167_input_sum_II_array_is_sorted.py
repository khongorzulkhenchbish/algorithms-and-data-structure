class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Brute-force approach would be to check sum of every possible pairs.
        2. Better approach would be to use hashmap to store the nums while iterating
        the arr and check if the num is in hashmap already. We store the hashmap such
        that { (target-curr):index_curr }
        3. As the elements are sorted, we should take advantage by using two pointers.
        Time: O(N), Space: O(1)
        """
        l = 0
        r = len(nums)-1

        while (nums[l]+nums[r] != target): # because we know there exist an answer
            if (nums[l]+nums[r] > target):
                r -= 1
            else:
                l += 1

        return [l+1, r+1]
        """
        nums = [1,2,5,6,7,11,15], target = 9
        l = 0,  0,  0, 1
        r = 6,  5,  4, 4
        s = 16, 12, 8, 9 => target => indexes [1,4] 
                                   => answer wants to start counting array from 1
                                   => return [2,5]
        """