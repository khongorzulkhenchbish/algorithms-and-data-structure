class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Optimal approach
        0 -> 0000 = 0   dp[1] = 0 + dp[0-0]
        1 -> 0001 = 1   dp[1] = 1 + dp[1-1] 
        2 -> 0010 = 1   dp[2] = 1 + dp[2-2]
        3 -> 0011 = 2   dp[3] = 1 + dp[3-2] 
        4 -> 0100 = 1   dp[4] = 1 + dp[4-4] 
        5 -> 0101 = 2   dp[5] = 1 + dp[5-4] 
        6 -> 0110 = 2   dp[6] = 1 + dp[6-4] 
        7 -> 0111 = 3   dp[7] = 1 + dp[7-4] 
        8 -> 1000 = 1   dp[8] = 1 + dp[8-8] 
        9 -> 1001 = 2   dp[9] = 1 + dp[9-8]  
        => dp[i] = (1 + dp[i-offset]) except i=0, offset=2**m

        Time: O(n), Space: O(n)
        """
        ans = [0]*(n+1)
        offset = 1  # max power of two at that time

        for i in range(1, n+1): # exclude 0 as added already
            if offset * 2 == i:
                offset = i  # offset is renewed at 4, 8, 16, 32 ...
            ans[i] = 1 + ans[i - offset]
        return ans

        """
        Naive apparoach
        Time: O(n*32) => O(nlogn)
        Space: O(n)
        arr = []
        for i in range(n+1):
            num = i
            count1 = 0
            while num != 0:
                count1 += num % 2
                num = num >> 1
            
            arr.append(count1)
        
        return arr
        """