class Solution:
    """
    Time: O(N), Space: O(logN), prefix sum, binary search
    Intuition: Imagine dividing a cake to people at the party in a way person with the highest weight
    gets the largest probability of picking the slices.

    Suppose we have people with weight [1,2,3,4,3] and we decided to order cake proportional to our
    total weight = 1+2+3+4+3 = 13 pound cake.

    This can be represented as [0, 1,1, 2,2,2, 3,3,3,3 4,4,4]. We want to get "slice randomly" and
    distribute the "human deterministically". Example: Chance of picking 2 slices is 3/13.

    So the slice 0 belongs to 0 pound guy.
           slice 1-2 belongs to 1 pound guy.
           slice 3-5 belongs to 2 pound guy.
           slice 6-9 belongs to 3 pound guy.
           slice 10-12 belongs to 4 pound guy.

    This pattern brings the prefixSum = [1,1+2,1+2+3, ..] = [1,3,6,10,13]
    """

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total_until = 0

        for weight in w:
            total_until += weight
            self.prefix_sums.append(total_until)

        self.total_sum = total_until

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        # input is sorted, binary search to find which index will be 
        # returned according to its probability, we search in the extended array
        # => [0, 1,1, 2,2,2, 3,3,3,3 4,4,4] => [0:1, 1:2, 2:3, 3:4, 4:3] => [1, 3, 6, 10, 13]
        # searching on prefix_sums=[1, 3, 6, 10, 13] is faster than on extended=[0, 1,1, 2,2,2, 3,3,3,3 4,4,4]
        left, right = 0, len(self.prefix_sums)

        while left < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1 # go to the right subarray
            else:
                right = mid # go to the left subarray
        
        return left

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()