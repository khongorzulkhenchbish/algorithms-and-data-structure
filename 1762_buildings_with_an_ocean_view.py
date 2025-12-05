class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
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