class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        It is important to first think a bit then notice the numbers:
        nums = [1 2 3 4 ... 100 ... 200] here we have 3 sequence, how do we know?
        We know the num is start of the sequence if num-1 doesn't exist in the nums.
        So, we go through each element then calculate the sequence length for sequence starters.
        '''
        numset = set(nums)
        answer = 0
        # faster to iterate in the numset
        for num in numset:  # O(N)
            if num-1 not in numset: # O(1) we found the starter of the sequence
                dist = 1            # we include the num itself in the length calculation
                while num + dist in numset: # O(N) we stop only when there is no more sequence element
                    dist += 1
                answer = max(answer, dist)
        
        return answer
        """ Example 1: nums = [100,4,200,1,3,2] => [1,2,3,4..100..200]
        numset = (100,4,200,1,3,2)
        100     start of a set  dist=1  answer = 1
        4       3 exists in the set, skip
        200     start of a set  dist=1  answer = 1
        1       start of a ser  dist=1,2,3,4    answer=4

        Example 2: nums = [0,3,7,2,5,8,4,6,0,1] => [0,0,1,2,3,4,5,6,7,8]
        numset = (0,3,7,2,5,8,4,6,1)
        0   start of a set  dist=1,2,3,4,5,6,7,8,9  ansnwer=max(0,9)=9

        Worst case: [4,3,2,1,0] answer=5 time = O(N+N) = O(N)
        """