class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Time: O(N * alpha(N)). This is practically O(N).
        # Space: O(N) to store the parents and sizes arrays.

        n = len(edges)
        # Using n+1 because nodes are 1-indexed
        parents = [i for i in range(n+1)]
        sizes = [1] * (n+1)

        def findp(i):
            if i == parents[i]:
                return i
            # Path Compression
            parents[i] = findp(parents[i])
            return parents[i]

        for n1, n2 in edges:
            p1, p2 = findp(n1), findp(n2)

            if p1 == p2:
                return [n1, n2]    # always keeps the last edge
                # there is no need to calculate the rest, because we know already its the last closing one
            
            # connect two nodes
            if sizes[p1] > sizes[p2]:
                parents[p2] = p1
                sizes[p1] += sizes[p2]
            else: # sizes1 <= sizes2
                parents[p1] = p2
                sizes[p2] += sizes[p1]

        return []