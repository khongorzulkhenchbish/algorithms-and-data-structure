import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Solution 1: Naive
        sort the arr
        return arr[-k]

        Solution 2: Heap, build on the go until k
        Time O(N * log k)
        Space O(k)
        After full loop, it will have full k largest list, return the smallest
        """
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                # store up to k items at the time
                heapq.heappush(min_heap, num)
            else:
                # remove elem then push another when storage length exceeds k
                heapq.heappushpop(min_heap, num)
        
        # root the is k-th from the largest
        return min_heap[0]
        """
        nums = [3,2,3,1,2,4,5,5,6], k = 4
        operation       | min_heap      | kth largest 
        push 3,2,3,1    | [1,2,3,3]     | 1
        pushpop 2       | [2,2,3,3]     | 2
        pushpop 4       | [2,3,3,4]     | 2
        pushpop 5       | [3,3,4,5]     | 3
        pushpop 5       | [3,4,5,5]     | 3
        pushpop 6       | [4,5,5,6]     | 4
        """