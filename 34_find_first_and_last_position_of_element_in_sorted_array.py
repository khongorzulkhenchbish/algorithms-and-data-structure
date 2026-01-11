class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left, right, leftbias):
            """ Brute-force to use two pointers and iterate both from left and right
            to find the two indexes in O(N) time. The contraints says to do it in logN
            time. Therefore, still use 2 pointers, but we have 3 cases.
            1. Both the start and end are on the left side of the array: [1,8,8|9,10,11]
               It means (mid_val > target), we want to go to the left
            2. Both the start and end are on the right side of the array: [2,3,4,5|7,8,8]
               It means (mid_val < target), we want to go to the right
            3. The start and the end are in the middle: [1,2,(8,8|8,)3,4,5]
               We have to go both ways. Doing so at the same time will make it complex.
               Trick:
               we call the subfunction itself twice, but first time, we intentionally go left.
               Second time, we intentionally go right. This way after two calls, we get the first
               and last position of the element in sorted array.

            Time: O(logN), Space: O(1) 
            """
            lastm = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:      # both are on the right side
                    left = mid + 1
                elif nums[mid] > target:    # both are on the left side
                    right = mid - 1
                else:                       # [1,2,8,|8|,8,8,4] go both side
                    lastm = mid
                    if leftbias:            # we go left most as we could
                        right = mid - 1
                    else:                   # we go right most as we could
                        left = mid + 1

            # return the last index of mid
            return lastm
                
        length = len(nums)-1
        minInd = binarySearch(0, length, True)
        maxInd = binarySearch(0, length, False)

        return [minInd, maxInd]

        # Linear time solution
        # i=0
        # while(i < len(nums) and nums[i]!=target):
        #     i+=1
        
        # j=len(nums)-1
        # while(j > -1 and nums[j]!=target):
        #     j-=1
        
        # if(j==-1):
        #     return [-1,-1]
        # return [i,j]