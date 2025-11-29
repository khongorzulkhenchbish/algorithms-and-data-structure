"""
subarray with the largest sum.
subarray is a contiguous part of an array.
array is not sorted and always not empty.

constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

why?
we have to check for every number in the array, whether to add it
in the existing subarray or start a new subarray with this number.

Kadane's Algorithm:
choise 1: extend maximum subarray ending at the prev element by adding
current element to it. If maxSubarraySum > 0, then extend the subarray.

choise 2: start a new subarray with the current element. If maxSubarraySum <= 0,
then start a new subarray.

Time complexity: O(n)
Space complexity: O(1)
"""
def maxSubarraySum(arr):

    # Store the result (max sum found so far)
    res = arr[0]

    # Max Sum of subarray ending at the current position
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        # Extend prev subarray or start new subarray

        # new subarray if current element is greater than
        maxEnding = max(maxEnding + arr[i], arr[i])

        # Update result if current subarray sum is found to be greater
        res = max(res, maxEnding)
    
    return res

"""
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6


arr[i] = 4
nums      = [-2,1,-3,4,-1,2,1,-5,4]
maxEnding = 5 (4, -1, 2, 1, -5, 4)
res       = 6 (4, -1, 2, 1) VS (4, -1, 2, 1, -5, 4)
"""