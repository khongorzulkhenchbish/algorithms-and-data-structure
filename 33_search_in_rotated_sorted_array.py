class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        same as 153? no. First find the pivot then do normal binary search
        Time: O(logn)
        Space: O(1)
        '''
        left, right = 0, len(nums)-1

        while left <= right:    # if odd elements then the mid elem won't be ignored
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            # are we in the left sorted portion?
            if nums[left] <= nums[mid]:
                # 456723, target=7,2 
                # L M TT
                # two cases when the target could be in the other side
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                
            # are we in the right sorted portion?
            else: # nums[left] > nums[mid]
                # 78123456, target=8,2
                # LTT M  R
                if target < nums[mid] or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1
