class Solution:
    def subarraySum(self, nums, k):
        """
        Intuition: Bit similar to Two Sum problem.
        Instead of checking all possible combinations, which
        will be O(N^2), we should store the prefix sum with how many times it appeared.
        The difference between currentSum and prefixSum will tell previously, how many
        times/sequences k was expressed in.
        nums = [1,-1,1,1,1,3]  k = 3
        curr_sum    dict
        1           {"1":1}    
        0           {"1":1, "0":1}
        1           {"1":2, "0":1}
        2           {"1":2, "0":1, "2":1}
        3           {"1":2, "0":2, "2":1, "3":1}    counter=1+1
        6           {"1":2, "0":2, "2":1, "3":1, "6":1}    counter=1+1+1
        """
        counter = 0
        curr_sum = 0
        sum_dict = {}
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum == k:
                counter += 1
            
            if (curr_sum - k) in sum_dict:
                counter += sum_dict[curr_sum - k]
            
            if curr_sum in sum_dict:
                sum_dict[curr_sum] += 1
            else:
                sum_dict[curr_sum] = 1

        # print(sum_dict)
        return counter

'''
Time Complexity: O(N) because taking sum of each n elements and lookup is O(1) with dictionary
Space complexity: O(N) because storing sum for each element in dictionary
'''