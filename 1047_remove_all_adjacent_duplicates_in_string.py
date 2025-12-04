class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Time: O(N), Space: O(N)
        
        The idea is the use stack so we can check the last added number always.
        str = "abbaca"
        ch = a      => b        => b              => a              => c     => a
        stack = [a] => [a,b]    => "b==b" pop(b)  => "a==a" pop(a)  => [c]   => [c,a] => "ca"
        """
        stack = []

        for char in s:
            if not stack: # if empty, just add the char
                stack.append(char)
            else:
                if char == stack[-1]: # compare with the last without removing anything from the stack
                    stack.pop() # last added out
                else:
                    stack.append(char) # added whatever unique
        
        # [c,a] => "ca"
        return "".join(stack)
        # for empty string, it will return ""