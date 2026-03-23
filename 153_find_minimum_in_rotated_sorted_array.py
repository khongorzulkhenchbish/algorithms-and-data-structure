class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        we can have 2 options after picking the middle element:
                min is on the right group | min is on the left group
                    456789123                891234567
                    L   M   R                L   M   R
                    4 < 8 => go right        8 > 3 => go left

        Time: O(logn)
        Space: O(1)
        '''

        n = len(nums)
        left = 0
        right = n-1
        minnum = nums[left]

        while (left < right):
            if nums[left] < nums[right]:            # if the array is sorted 12345
                minnum = min(minnum, nums[left])    # then it must be updated
                break

            mid = right + left // 2
            minnum = min(minnum, nums[mid])

            # determine if we will search to the left or right
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minnum