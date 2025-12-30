class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Space: O(N-numbers), Time: O(N)
        # In reverse Polish notation, the operators follow their operands. 
        # The conventional notation expression 3 − 4 + 5 becomes 3 (enter) 4 − 5 + in 
        # reverse Polish notation: 4 is first subtracted from 3, then 5 is added to it.
        # The advantage of reverse Polish notation is that it removes the need for 
        # order of operations and parentheses that are required by infix notation 
        # and can be evaluated linearly, left-to-right. For example, the infix expression 
        # (3 + 4) × (5 + 6) becomes 3 4 + 5 6 + × in reverse Polish notation.
        # Therefore storing the numbers in the stack until the operand is read, once the operands are present
        # we can execute the operation and push the value back to the stack.
        stack = [] 
        
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                # add all numbers
                stack.append(int(token))
            else:
                # execute the operations
                r = stack.pop()
                l = stack.pop()
                if token == '+':
                    stack.append(l+r)
                elif token == '-':
                    stack.append(l-r)
                elif token == '*':
                    stack.append(l*r)
                else: # must be the division, to avoid truncation to zero, we will get float value
                    stack.append(int(float(l)/r))
        # last expression adds the last value in the stack
        return stack.pop()
        """
        tokens = [3, 4, +, 5, 6, +, ×]
        stack = [3, 4] => operand +, l = 3, r = 4 => [7]
                [7, 5, 6] => operand +, l = 5, r = 6 => [7, 11]
                operand *, l = 7, r = 11 => [77] => pop answer = 77
        """
                    
        