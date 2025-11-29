class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, tSum = 0, 0
        sumMap = {} 
        sumMap[0] = 1 
        for i in range(len(nums)):
            tSum += nums[i]
            if (tSum - k) in sumMap:
                count += sumMap[tSum - k]
            if tSum in sumMap:
                sumMap[tSum] = sumMap[tSum] + 1
            else:
                sumMap[tSum] = 1
        return count

#Time Complexity: O(N) because taking sum of each n elements and lookup is O(1) with dictionary

#Space complexity: O(N) because storing sum for each element in dictionary
