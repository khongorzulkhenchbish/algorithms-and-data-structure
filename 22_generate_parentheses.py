class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        '''
        n = 1 pairs, ()
        n = 2 pairs, ()()   (())
        n = 3 pairs, ((())) (()()) ()(()) ()()() (())()
        Time: 2 branches always almost O(2^N)
        Space: O(N) at longest, we will store (2*N)
        '''
        ans, sol = [], []

        def backtrack(opening = 0, close = 0):
            # print(S, opening ,close)
            if len(sol) == 2*N:
                ans.append(''.join(sol))
                return
            
            # IF AND ONLY IF opening BRACKET IS MORE THAN 
            # CLOSING AND LESS THAN N
            if opening < N:
                sol.append("(")
                backtrack(opening+1, close)
                sol.pop()
                
            # opening BRACKET IS FULL OR MORE THAN CLOSING
            # to close something we should have the opening for it
            # already
            if opening > close:
                sol.append(")")
                backtrack(opening, close+1)
                sol.pop()

        backtrack()
        return ans