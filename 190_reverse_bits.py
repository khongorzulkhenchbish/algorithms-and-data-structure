class Solution:
    def reverseBits(self, n: int) -> int:
        # Time: O(1), Space: O(1)
        reverse = 0

        # Do the following 32 times (because we have 32 right_most integer)
        for i in range(32):
            
            # left shift to reverse
            reverse = reverse << 1
            # add the rightmost on the reverse
            right_most = n % 2
            reverse += right_most
            # remove the rightmost from n
            n = n >> 1

        return reverse
        # Sample:
        # Input: 1010

        #   reverse<<1        reverse+=n%2       n>>1
        #           00                  00        101
        #          000                 001         10
        #         0010                0010          1
        #        00100               00101          _