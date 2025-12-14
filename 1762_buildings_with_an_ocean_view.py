class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Constraint: iterate from the left only!
        Use monotonic stack. The diff between monotonic stack vs normal stack
        is the order. If it is continuely inc/decreasing.
        Time: O(N), Space: O(N)
        """
        inc_stack = []
        for i in range(len(heights)):
            # <= because when [2,2,2,2] => then only the 3rd indexed 2 can see the ocean 
            while inc_stack and heights[inc_stack[-1]] <= heights[i]:
                # because heights[i] will block the top element
                inc_stack.pop()

            # either the stack is empty, or the elems can see the ocean
            inc_stack.append(i)
        
        return inc_stack

        """
        No Constraint
        Time: O(n), Space: O(N) if we have all having ocean view
        What if instead we look from the right to the left and only add those higher 
        than our max?
        [4,8,5,3,7,3,5,1] => [3,7]
        """
        length = len(heights)
        oceanview = [length-1]

        # we start the iteration from the second last because
        # the last will always be able to see the ocean and
        # if we start iteration from the last,
        # then it will have nothing prev before to be compared
        for i in range(length-2, -1, -1):
            # add only when we find higher/lower from the left/right to right/left
            if heights[i] > heights[oceanview[-1]]:
                oceanview.append(i)
        
        # in-place reverse method
        oceanview.reverse()
        return oceanview