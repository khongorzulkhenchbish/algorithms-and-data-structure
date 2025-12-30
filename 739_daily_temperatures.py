class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        # Monotonic stack
        # Time: O(n)
        # Space: O(m) worst scenario is 1*m [4,3,2,1], best scenario m length array [1,2,3,4]
        ans = [0] * len(nums)

        index_stack = []
        index_stack.append(0) # idx of the first element

        for i in range(1, len(nums)):
            # always compare the latest found number without ans with current one
            while index_stack and nums[index_stack[-1]] < nums[i]:
                # abstraction, diff between 2 position
                ans[index_stack[-1]] = i - index_stack[-1]
                index_stack.pop() # remove the element because ans was calculated
            index_stack.append(i) # use the index instead of the val, add until higher val appears
        return ans
        """ temperatures = [73,74,75,71,69,72,76,73]
        i = 1   index_stack = (0)   74>73       ans = [1]             =>  index_stack.pop.append(1) => (1)
        i = 2   index_stack = (1)   75>74       ans = [1, 1]          =>  index_stack.pop.append(2) => (2)
        i = 3   index_stack = (2)   71>75                                 index_stack.append(3)
        i = 4   index_stack = (2, 3)    69>71                             index_stack.append(4)
        i = 5   index_stack = (2, 3, 4) 72>69   ans = [1, 1, 0, 0, 1] =>  index_stack.pop()
        i = 5   index_stack = (2, 3)    72>71   ans = [1, 1, 0, 2, 1] =>  index_stack.pop()
        i = 5   index_stack = (2)   72>75                                 index_stack.append(5)
        i = 6   index_stack = (2,5) 76>75       ans = [1, 1, 0, 2, 1, 1]=>index_stack.pop()
        i = 6   index_stack = (2)   76>75       ans = [1, 1, 4, 2, 1, 1]=>index_stack.pop.append()
        i = 7   index_stack = (6)   73>76                               =>index_stack.append(7)
        i = 8   index_stack = (6,7)             ans = [1, 1, 4, 2, 1, 1, 0, 0]
        """
        # Brute force
        # Time complexity: O(n^2)
        # Time limit exceeded
        # ans = [0] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             ans[i]=j-i
        #             break
        # return ans