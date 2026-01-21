class Solution:
    def decodeString(self, s: str) -> str:
        """ The problem gets difficult because of the nested input.
        The recursive approach could work but can be complicated.

        We will store everything in the stack as long as we don't see ].
        Once we encounter "]", we should solve the subproblems from back to front
        direction. k[a[]b[]c[]] then we will solve in order c[] => b[] => a[] => k[]
        
        What do we know as true:
        - before brackets, there will be number always

        Example: 54[ab6[cd]] => stack=54[ab6 [cd] => detected ] => 
        stack=54ab cdcdcdcdcdcd => ] detected
        stack=54*(abcdcdcdcdcdcd)

        Time: depends on the input
        Space: depends on the input
        """ 
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else: # reverse pop until [
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr # add letters reverse order
                # we have the substr, now pop the "["
                stack.pop()

                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count # add frequency in reverse order
                # we have the countetition number

                # append the nested => substr*count to the stack
                stack.append(int(count) * substr)
        
        # stack will contain the decoded original str
        return "".join(stack)
        """
        s = "3[a2[c]]"
        i = 0, 1, 2, 3, 4, 5, 6
        stack = (3,[,a,2,[,c)
        stack = (3,[,a,2,[)        subs = "c"
        stack = (3,[,a)            count = "2"
        stack = (3,[,a,c,c)
        i = 7
        stack = (3,[,a,c,c)        subs = ""
        stack = (3,[,a,c,)         subs = "c"
        stack = (3,[,a,)           subs = "cc"
        stack = (3,[,)             subs = "acc"
        stack = (3,)               subs = "acc"
        stack = ()                 count = "3"
        stack = (accaccacc)        => answer = "accaccacc"
        """