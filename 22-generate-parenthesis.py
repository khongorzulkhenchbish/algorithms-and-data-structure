Problem 1. 22. Generate Parentheses
Solution 1. '''
Instead of adding '(' or ')' every time, let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.
We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
'''

class Solution(object):
    def generateParenthesis(self, N): 
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            
            if len(S) == 2 * N: # 4 == 6 
                ans.append(S)
                return
            
            # IF AND ONLY IF OPENING BRACKET IS MORE THAN CLOSING AND LESS THAN N
            
            if left < N: 

                backtrack(S+'(', left+1, right) 
            
            #OPENING BRACKET IS FULL OR MORE THAN CLOSING   
            if right < left: # 2 < 3
                
                backtrack(S+')', left, right+1) 
                
                

        backtrack()
        return ans
"""
["((()))","(()())","(())()","()(())","()()()"]

backtrack(‘(‘, 1, 0)

1)  backtrack(‘((‘, 2, 0)

        1.1) backtrack(‘(((‘, 3, 0)                    -> ((())) - sol 1
                
        1.2) backtrack(‘(()‘, 2, 1)
        
                1.2.1) backtrack(‘(()(‘, 3, 1)
                
                    1.2.1.2) backtrack(‘(()()‘, 3, 2)        -> (()())- sol 2
                        
                1.2.2) backtrack(‘(())‘, 2, 2)
                    
                    1.2.2.1) backtrack(‘(())(‘, 3, 2)   -> (())() - sol 3
                            
                
2)  backtrack(‘()‘, 1, 1)

    2.1)  backtrack(‘()(‘, 2, 1)
    
        2.1.1) backtrack(‘()((‘, 3, 1)
        
            2.1.1.1) backtrack(‘()(()‘, 3, 2)
            
                2.1.1.1.2) backtrack(‘()(())‘, 3, 3)  - ()(())- sol 4
            
        2.1.2) backtrack(‘()()‘, 2, 2)
        
            2.1.2.1) backtrack(‘()()(‘, 3, 2)
            
                2.1.2.1.2) backtrack(‘()()()‘, 3, 3) - ()()()- sol 5
            
"""
