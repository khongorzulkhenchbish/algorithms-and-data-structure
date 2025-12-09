class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Optimal Approach: Time: O(N), Space: O(N)
        # first build list for minHeap
        minHeap = []
        for x,y in points:
            dist = (x**2 + y**2)
            minHeap.append([dist, x, y])
        
        # creates a minimum heap from the list in linear time
        # heap uses the first index as the sorting point
        heapq.heapify(minHeap)

        # return the k smallest items
        k_list = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            k_list.append([x, y])
            k -= 1

        return k_list

        # # Approach 1 - Time: O(NlogN), Space: O(1)
        # # Sort the list with a custom comparator function
        # points.sort(key=self.squared_distance)
        
        # # Return the first k elements of the sorted list
        # return points[:k]
        
        # def squared_distance(self, point: List[int]) -> int:
        #     """Calculate and return the squared Euclidean distance."""
        #     return point[0]**2+point[1]**2