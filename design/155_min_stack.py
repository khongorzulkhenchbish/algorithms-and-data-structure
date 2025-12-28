class MinStack:
    def __init__(self):
        # In this solution, you can either have 2 stacks, where the second one stores the min elems
        # alongside the curr elements, or just one stack with tuple items - (curr, min_curr)
        # Space complexity is O(N) for both data structures. Time: O(1) for each method.
        self.minStack = []

    def push(self, val: int) -> None: # O(1)
        # The intuition is to save the minimum element at each step as well, so when we call the
        # getMin, we should be able to return in O(1) time.
        minval = val # by default, curr elem is the min
        if self.minStack:
            minval = min(self.minStack[-1][1], val) # update if the prev elem in stack is less than curr
        self.minStack.append((val, minval)) # store ass tuples

    def pop(self) -> None:
        self.minStack.pop() # O(1)

    def top(self) -> int:
        return self.minStack[-1][0] # O(1)

    def getMin(self) -> int:
        return self.minStack[-1][1] # O(1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()