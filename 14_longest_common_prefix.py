class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ We want to check that for every string, the letters match.
        [f]lower
        [f]low
        [f]light
        We traverse index i goes between 0-len(s).
        Then we will face problem with length reaching first with flo[w]. Out of bound.
        Time: O(N*shortest length of subs) Space: O(m) at worst when all of them equal
        """
        common = ""

        for i in range(len(strs[0])): # we start with "flower"
            for s in strs: # we go through [flow, flight] or 
                if i == len(s) or s[i] != strs[0][i]:
                    # if we reaches the shortest, we don't have to go forward anymore
                    # or if we find a mismatching character, we don't have to go forward
                    return common
                else:
                    pass # continues to check i-th matching char for the [flow, flight]
            # after 1 iteration, here i-th char will be same for all strs array.
            common += strs[0][i] # we add from the first string, or any of the subs
            # i will increase and we look for i+1 through all of the strs array elements
        return common
        

        # Approach: Brute force, Time: O(N^2)
        # common = ""

        # if len(strs) == 1:
        #     return strs[0]

        # first = strs[0]
        # second = strs[1]
        # i = 0
        # while i < len(first) and i < len(second) and first[i]==second[i]:
        #     i += 1
        
        # first = second
        # common = first[:i]

        # for second in strs[2:]:
        #     i = 0
        #     while i < len(first) and i < len(second) and first[i]==second[i]:
        #         i += 1
        #     first = second
            
        #     if i < len(common):
        #         common = second[:i]
        
        # return common