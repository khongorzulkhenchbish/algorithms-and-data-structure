class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ The intuition is to oversee the board and realize that we need to have fixed element
        on the left side already. The a second pointer that moves to the right. We can update the
        nums only when there is a number not equal to the fixed one.

        Time: O(N)
        Space: O(1) no extra space
        """
        left = 0
        for right in range(left+1, len(nums)):
            if(nums[left] == nums[right]):
                pass # we just wait to compare current with the next ones in the array
            else:
                left += 1
                nums[left] = nums[right]
            
        return left+1
        """
        nums = [0,0,1,1,1,2,2,3,3,4]
        left = 0, 1, 2, 3, 4
        right = 1, 2, 3, 4, 5, 6, 7, 8, 9
        nums_left = [0,1,2,3,4..,2,2,3,3,4]
        """
        