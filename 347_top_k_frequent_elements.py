import heapq

class Solution:
    def topKFrequent(snumf, nums: List[int], k: int) -> int:
        # Linear time solution: bucket sort
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
        # time: O(N), space: O(N)
        for i in range(len(buckets)-1, 0, -1):
            # although it seems like nested loop, the time will be O(n+n)
            while buckets[i]:
                kmost.append(buckets[i].pop())
                if len(kmost) == k:
                    return kmost
        
        return []


        # Heap solution - # Time O(N*logK), Space O(K)
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        # Solution 1: heap
        min_heap = []
        for key, val in counter.items():
            if len(min_heap) < k:
                # insert into the heap to be sorted by first(val) of the tuple
                heapq.heappush(min_heap, (val, key))
            else:
                # heap is exactly k
                heapq.heappushpop(min_heap, (val, key))
        
        return [h[1] for h in min_heap]
        """
        nums = [1,2,1,2,1,2,3,1,3,2], k = 2
        counter = {"1":4, "2":4, "3":2}
        min_heap = [(4,1), (4,2), (2,3)] store only k => [(4,1), (4,2)]
        return first(val) only from the tuples => [1, 2]
        1 and 2 are the k=2 elements which appeared the most.
        """