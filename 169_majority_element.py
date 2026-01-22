class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ Boyer-Moore algorithm. Time: O(N), Space: O(1)

        We keep a counter and assume the first num is the majority. Once we reach a diff num than assumed one,
        we should decrease the counter. If the counter becomes 0, then it means, current number is the longest
        so far.
        nums = [2,2,1,1|1,2,2,2,2]  majority=2 counter=0 so we reset majority to 1
        nums = [2,2,1,1,1|2,2,2,2]  majority=1 counter=1 
        nums = [2,2,1,1,1,2|2,2,2]  majority=1 counter=0 reset majority=2 as by this point 
                                    2's freq == 1's freq, 2 could be the longest.
        ...
        nums = [2,2,1,1,1,2,2,2,2|] majority=2 counter=3  2 appeared 3 more than 1.
        """
        majority = nums[0]
        counter = 1

        for num in nums[1:]:
            if counter == 0: # we've found another number that is longest
                majority = num
        
            if num == majority:
                counter += 1
            else: # we've found a new number
                counter -= 1

        return majority
        # 2,2,1,1|1,2,2
        # counter = 1, majority = 2, num = 2, at the end the diff of freq 2 appeared 4 times, 1 appeared 3 times
        # 6,5,5
        # counter = 0, majority = 5, num = 5,

        # Approach: Time: O(N), Space: O(N)
        # freq = {}
        # for num in nums:
        #     freq[num] = 1 + freq.get(num, 0)
        
        # for num, count in freq.items():
        #     if count > (len(nums) // 2):
        #         return num
        
        # return