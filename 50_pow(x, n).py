class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Time: O(logN), Space: O(logN)
        Intuition:
        2^100 = 2*2* ... * (100 multiplications) => O(N)
        
        What if
        2^100   = (2∗2)^50          100 -> 50 = even -> even
        4^50    = (4∗4)^25          50  -> 25 = even -> odd
        16^25   = 16∗(16)^24        25  -> 12 = odd -> even
        16^25   = 16∗(16∗16)^12     
        ...
        2^100   = 1267650600228229401496703205376
        """
        # base condition
        if n == 0:
            return 1
        
        # negative
        if n < 0:
            # it enough to turn the minus sign to plus, it will run just once
            # turning - degree into subproblem of 1/myPower(num, positive sign)
            return 1 / self.myPow(x, -1*n)
        
        # positive, even
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        # positive, odd
        else:
            return x * self.myPow(x*x, (n-1)/2)
        """
        Example 1: x = 2.0, n = 3
        n is odd => 2*myPow(4, 1) => n is odd => 2*4*myPow(16, 0) => n is 0 => 8

        Example 2: x = 2.0, n = -3
        n is neg => 1/myPow(2, 3) => 1/8
        """