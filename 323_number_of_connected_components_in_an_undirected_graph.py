class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Approach 2. Union find. 
        # Time: O(V + E*alpha(V)), where alpha is that near-constant Inverse Ackermann function.
        #       This is significantly faster than any manual set-merging logic.
        # Space: O(V) to store the parent array.

        # initially every i is its own king
        parents = [i for i in range(n)]
        # rank is the height of the trees
        rank = [1] * n 

        def findParent(i):
            while i != parents[i]:
                parents[i] = parents[parents[i]] # path compression
                i = parents[i]
            return i
        
        def union(n1, n2):
            parent1, parent2 = findParent(n1), findParent(n2)

            if parent1 == parent2:
                return 0
        
            if rank[parent2] > rank[parent1]:
                # integrate the smaller tree into larger one by assigning the parents index
                parents[parent1] = parent2
                # and incrementing the height of the parent
                rank[parent2] += rank[parent1]
            else:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]

            return 1

        result = n
        for n1, n2 in edges:
            # for every nodes, decrement by the edge number.
            # if they are connected, then the edge will be 1
            result -= union(n1, n2)
        
        return result

        # Approach 1. DFS. time: O(V+E), space: O(V+E)
        # adj = { i:[] for i in range(n) }

        # for anode, bnode in edges:
        #     adj[anode].append(bnode)
        #     adj[bnode].append(anode)
        
        # count = 0
        # visited = set()
        # def dfsPaint(currNode):
        #     if currNode in visited:
        #         return
            
        #     visited.add(currNode)

        #     for neighbor in adj[currNode]:
        #         dfsPaint(neighbor)
        
        # for currNode in adj:
        #     if currNode not in visited:
        #         count += 1
        #         dfsPaint(currNode)
        
        # if edges:
        #     return count
        # else:
        #     return n