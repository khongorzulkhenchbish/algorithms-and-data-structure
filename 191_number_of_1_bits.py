class Solution:
    def hammingWeight(self, n: int) -> int:
        # Space: O(1)
        count = 0
        while n: # stop at zero 
            """
            count = 0
            # We loop 32 times to check every bit in a 32-bit integer
            for i in range(32):
                # 1. Check the last bit
                # (n & 1) will countult in 1 if the last bit is 1,
                # and 0 if the last bit is 0.
                count += (n & 1)
                
                # 2. Shift all bits to the right by one
                # This moves the next bit into the last position.
                n = n >> 1     
            return count
            Example: START n = 15
            Step 1: count += (0111 & 0001)  => 0001 => count=1
                    n = 0111 >> 1           => 0011 => n=0011
            Step 2: count += (0011 & 0001)  => 0001 => count=2
                    n = 0011 >> 1           => 0001 => n=0001
            Step 3: count += (0001 & 0001)  => 0001 => count=3
                    n = 0001 >> 1           => 0000 => n=0 END
            """

            """
            Option 2: Brian Kernighan's Algorithm
            Time: O(1) but runs number of times one occurs only.
            Example: (n = 130) => 128+2 => 10000001 => should be solved in only 2 steps
            Step 1: n = 10000001 & (10000000) => 10000000  whatever happens count+1
            Step 2: n = 10000000 & (01111111) => 00000000  whatever happens count+1
            """
            n = n & (n - 1) 
            count += 1
        return count