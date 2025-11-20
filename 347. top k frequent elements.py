import heapq

class Solution:
    def topKFrequent(snumf, nums: List[int], k: int) -> int:
        # time: O(n) with bucket sort, space will be O(n)
        # nums = [1,1,1,2,2,100]
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # creates the empty bucket
        buckets = [[] for i in range(len(nums)+1)]


        for key, val in freq.items():
            # reversing the hashmap we created.
            # val will the be index/frequency of how many times the key appeared
            buckets[val].append(key)
            # ["1":3, "2":2, "100":1] => [[], [100], [2], [1]]
        
        # traverse backwards because the freq is decreasing by index
        kmost = []
        # time: O(n)
        for i in range(len(buckets)-1, 0, -1):
            # although it seems like nested loop, the time will be O(n+n) 
            while buckets[i]:
                kmost.append(buckets[i].pop())
                if len(kmost) == k:
                    return kmost
        
        return []


        # Heap solution - O(n*logn)
        # counter = {}

        # for num in nums:
        #     counter[num] = 1 + counter.get(num, 0)

        # Solution 1: heap
        # heap = []
        # for key, val in counter.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (val, key))
        #     numse:
        #         # heap is exactly k
        #         heapq.heappushpop(heap, (val, key))
        
        # return [h[1] for h in heap]

        # Time O(N*logK)
        # Space O(N)