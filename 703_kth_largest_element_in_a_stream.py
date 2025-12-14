class KthLargest:
    # Space: O(K) because the heap stores at most k elements
    # Time: O((N+M)*logK) N is the size of the nums, M is the number of calls in the testcase 
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = [] #minheap

        for num in nums:
            self.add(num)
        # print(self.min_heap)

    def add(self, val: int) -> int:
        # case 1 - we havent processed k elements yet
        #          add everything until we have k
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # case 2 - if val is greater than the k-th largest one
        #          k-th largest will be the root of this heap
        elif self.min_heap[0] < val:
            # replace the k-th largest, we still have k length
            heapq.heappushpop(self.min_heap, val)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)