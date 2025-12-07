class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition:
        For every number we have 2 options.
        Include in the subset or NOT include the subset => Backtracking
        The overall check will be O(n*2^n)
        """
        subsets = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return subsets
"""
nums = [1,2,3]
dfs(0) => dfs([1], 1) => dfs([1,2], 2) => dfs([1,2,3], 3) => subsets=[[1,2,3]]
                                       => dfs([1,2], 3) => subsets=[[1,2,3],[1,2]]
                      => dfs([1], 2)   => dfs([1,3], 3) => subsets=[[1,2,3],[1,2],[1,3]]
                                       => dfs([1], 3)   => subsets=[[1,2,3],[1,2],[1,3],[1]]
          dfs([ ], 1) => dfs([2], 2)   => dfs([2,3], 3) => subsets=[[1,2,3],[1,2],[1,3],[1],[2,3]]
                                       => dfs([2], 3)   => subsets=[[1,2,3],[1,2],[1,3],[1],[2,3],[2]]
                      => dfs([], 2)    => dfs([3], 3)   => subsets=[[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3]]
                                       => dfs([], 3)    => subsets=[[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]

"""