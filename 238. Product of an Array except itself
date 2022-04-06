class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # S imply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
    
    '''
    Input = [1, 2, 3, 4]
    # on first iteration (get product of all left elements for each element)
    ans[1] = nums[0] * ans[0] = 1 * 1 = 1
    ans[2] = nums[1] * ans[1] = 2 * 1 = 2
    ans[3] = nums[2] * ans[2] = 3 * 2 = 6
    ans = [1, 1, 2, 6] (product of all left elements)
    
    
    # on second iteration (get product of all right elements for element)
    R = 1
    ans[3] = ans[3] * R = 6 * 1 = 6
    
    R = R * nums[3] = 1 * 4 = 4
    ans[2] = ans[2] * R = 2 * 4 = 8
    
    R = R * nums[2] = 4 * 3 = 12
    ans[1] = ans[1] * R = 1 * 12 = 12
    
    R = R * nums[1] = 12 * 2 = 24
    ans[0] = ans[0] * R = 1 * 24 = 24
    
    ans = [24, 12, 8, 6]
    '''

# Time Complexity: O(2N) = O(N) because iterating elements from left to right, then right to left, also each access time is O(1)

# Space Complexity: O(N) because answer array has N elements    
