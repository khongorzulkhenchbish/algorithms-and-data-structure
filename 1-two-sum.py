class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        imap = {}
        
        for i in range(len(nums)):
            
            complement = target - nums[i]
            if complement in imap:
                return [i, imap[complement]]
            imap[nums[i]]=i
            
        return false
        # [1,3,2,5,4] target = 8 ans = [3, 1]
        # nums[i] = 5
        # complement = 3
        # imap = {"1": 0, "3": 1, "6": 2, }

Time: O(n) because we go for each element and look up time for dictionary is O(1)
Space: O(n) because dictionary takes at most n element when there is no such pair

