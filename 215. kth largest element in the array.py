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
                heapq.heappush(min_heap, num)
                heapq.heappop(min_heap)
                # alternative => heapq.heappushpop(min_heap, num)
        
        # root the is k-th from the largest
        return min_heap[0]