class Solution:
    def calculate(self, s: str) -> int:
        # Time: O(N), Space: O(1) 
        if not s: return 0
        
        last_op = "+"   # We assume the first number has a '+' before it.
        total_sum = 0   # safe, stores only the addition/subtractions that are finished
        last_term = 0   # working area, result of the current multiplication/division
        curr_num = 0
        # (2 * 3 + 4 * 5)
        
        for i, char in enumerate(s):
            # Build the number (handles multi-digits like "42")
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            # If it's either * or /, we should reduce from 3+2*4 to 3+8
            if char in "+-*/" or i == len(s) - 1:
                if last_op == "+": # last_term is safe
                    total_sum += last_term
                    last_term = curr_num
                elif last_op == "-":
                    total_sum += last_term
                    last_term = -curr_num
                elif last_op == "*":    # do the operation immediately but don't add to the total_sum yet
                    last_term *= curr_num
                elif last_op == "/":
                    last_term = int(last_term / curr_num)
                
                # Only update operator if we are NOT at the very end
                last_op = char
                curr_num = 0

        return total_sum + last_term

        # Time: O(N) one traversal, Space: O(N) for the worst (-,+) cases, we end up storing all
        if not s:
            return 0
        
        stack = []
        curr_num = 0
        last_op = '+' # We assume the first number has a '+' before it
        operators = {'+', '-', '*', '/'}
        
        for i, char in enumerate(s):
            # 1. Build the number (handles multi-digits like "42")
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            # 2. If it's an operator OR we reached the very last character
            if char in operators or i == len(s) - 1:
                if last_op == '+':
                    stack.append(curr_num)
                elif last_op == '-':
                    stack.append(-curr_num)
                elif last_op == '*':
                    stack.append(stack.pop() * curr_num)
                elif last_op == '/':
                    # In Python, -3 // 2 is -2. 
                    # For this problem, we need truncation toward zero (-1).
                    top = stack.pop()
                    stack.append(int(top / curr_num))
                
                # Update for the next number
                last_op = char
                curr_num = 0

            # whitespaces are simple skipped
                
        return sum(stack)