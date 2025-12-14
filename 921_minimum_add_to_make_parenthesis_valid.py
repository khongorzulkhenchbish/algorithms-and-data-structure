class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Time: O(N), Space: O(1)
        ))(( => 4
        open = 0, 1, 2
        close= 2, => ans = open+close=4

        (())) => 
        open = 2, 1, 0,  
        close= x, x, 1 => answer=open+close=1

        empty => open+close=0
        """
        opening = 0
        closing = 0
        for ch in s:
            if ch == "(":
                opening += 1
            else: # closing
                if opening > 0:
                    opening -= 1
                else:
                    closing += 1
        
        return opening+closing
