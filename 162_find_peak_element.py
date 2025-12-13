class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Optimal approach - Time: O(logN), Space: O()
                   _
           _      / \
          / \    /   \ 
        _/   \__/     \_
        => imagine the nums as mountain, we need to return any of the peak
        """
        left = 0
        right = len(nums)-1

        
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                # if it is increasing to the left side -> left:mid
                right = mid
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                # if it is increasing to the right side -> mid:right
                left = mid+1
            else:
                # mid is either, first or last elem, or just inside the range. 
                # nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
        """
        Example 1:
        nums=[1], left=0, right=0, mid=0, RETURN 0
        
        Example 2:
        nums=[1,3], left=0, right=1, mid=0 => left=1, right=1, mid=1 => RETURN 1

        Example 3:
        nums=[3,2], left=0, right=1, mid=0 => RETURN 0

        Example 4:
        nums = [1,2,1,3,5,6,4], left=0, right=6, mid=3 =>
        nums = [5,6,4]        , left=4, right=6, mid=5 => RETURN 5

        """


        """
        [1,2,3,1]
        prev = -inf
        curr = 1
        next = 2
        if curr == 0 => prev = -inf
        if prev < curr > next => save peak index
        if next == n-1 => -inf

        [1]
        prev = -inf
        curr = 1
        next = -inf => 0 is peak index

        Naive approach - Time: O(N), Space: O(1)
        for i in range(len(nums)):
            if i == 0:
                prev = float(-inf)
            else:
                prev = nums[i-1]
            
            curr = nums[i]

            if i == len(nums)-1:
                nxt = float(-inf)
            else:
                nxt = nums[i+1]
            
            if prev < curr and curr > nxt:
                return i
        """