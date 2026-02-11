class Solution:
    """ The scale of the input 10^9 because each number can have up to 10^5 repetition
    Time: O(N) for init, O(logN) for pickIndex
    Space: O(N), prefix sum, binary search

    Intuition
    given array:                                   [1, 200,  3,   1,   2]
    1. assign indexes                              [0,  1,   2,   3,   4]
    2. prefix sum represents the weight, frequency [0, 201,  204, 205, 207]
    """
    def __init__(self, w: List[int]):
        self.prefix = []
        total_until = 0

        for weight in w:
            total_until += weight
            self.prefix.append(total_until)

        self.total_sum = total_until

    def pickIndex(self) -> int:
        # uniform will return number between 0, N with equal distribution.
        target = random.uniform(0, self.total_sum)
        # target will be between [0, 207] and we have to return the index where the val == target
        # target can be 105 for example.

        # input is sorted, binary search to find which index will be 
        # returned according to its "WEIGHT (probability)", we search in the extended array
        # searching on prefix=[0,201,204,205,207] is faster than on extended=[0, 1,1..(200X), 2,2,2, 3, 4,4]
        left, right = 0, len(self.prefix)

        while left < right:
            mid = (left + right) // 2
            if target > self.prefix[mid]:
                left = mid + 1 # go to the right subarray
            else:
                right = mid # go to the left subarray
        # target = 105
        # left = 0, 1
        # right = 5, 2, 1
        # mid = 2 => (105 < 204), 1 => (105 < 201), 0 => (105 < 0) not ==> left == right => 1
        # prefix_array = [0, 201, 204, 205, 207]
        # 1 being return value means, 105 is between [0,201] and in the og_arr=[1,200,....] 200 has the
        # most frequence and should be picked the most.
        return left