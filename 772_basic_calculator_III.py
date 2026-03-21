# based on solution of Basic Calculator II, but with recursion to handle parentheses
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        # Convert string to a deque so we can "pop" from the front in O(1)
        # This removes the need for index management!
        tokens = deque(s)
        
        # Time: O(n) - we process each character once
        # Space: O(n) - (Stack + Recusion + Queue) in worst case,
        # if we have a lot of nested parentheses and numbers, 1+2+3+...+n, etc.
        def parse():
            stack = []
            curr_num = 0
            prev_sign = "+"

            # calc everything until ")" or end of string (if there is no parenthesis at all)
            while tokens:
                char = tokens.popleft()

                # form the current number. eg: "123"
                if char.isdigit():
                    curr_num = curr_num * 10 + int(char)
                
                if char == "(":
                    # RECURSION: Solve the sub-expression inside the parentheses
                    curr_num = parse()

                # Check if we should process the current number
                # We do this if it's an operator, a closing bracket, or end of string
                if char in "+-*/)" or not tokens:
                    if prev_sign == "+":
                        stack.append(curr_num)
                    elif prev_sign == "-":
                        stack.append(-curr_num)
                    elif prev_sign == "*":
                        stack[-1] = stack[-1] * curr_num
                    elif prev_sign == "/":
                        stack[-1] = int(stack[-1] / curr_num)

                    if char == ")":
                        break # Return to the parent call immediately
                    
                    prev_sign = char
                    curr_num = 0
            
            
            return sum(stack)
       
        return parse()


if __name__ == "__main__":
    s1 = "1+(2*3)-(4/2)"
    s2 = "1+1"
    s3 = "(7+(6-5))/2"
    s4 = "2*(5+5*2)/3+(6/2+8)"

    print(s1, "=", Solution().calculate(s1))   
    print(s2, "=", Solution().calculate(s2))
    print(s3, "=", Solution().calculate(s3))
    print(s4, "=", Solution().calculate(s4))        
