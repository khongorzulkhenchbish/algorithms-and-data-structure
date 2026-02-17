class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        '''TODO: come back once practicing graph questions
        How to check if one circle contains anothers center?
        - answer is the calc the dist which is the pythogoras theorem.
        How do we follow that if circle a detonates b, then would circle b detonas a or c?
        - we will use it in data structure called adjacency list, where we will store
        - the detonated ones by current circle/node. thus, this is a graph problem, the edges are
        - directed. Time: O(n^3), Space: O(n^2)
        '''
        adj = collections.defaultdict(list) # every bomb corresponds to -> [list of bombs]
        
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
                
                # the edges are directed, following is obvious if you draw out the example 3.
                if dist <= r1:
                    adj[i].append(j) 
                    # the second bomb falls under the radius of the first one
                    # bomb[i] can detonate bomb[j]
                if dist <= r2:
                    adj[j].append(i) # bomb[j] can detonate bomb[i]
        
        def dfs(i, visit):
            if i in visit:
                return 0 # we can't detonate anymore
            visit.add(i)
            for neigh in adj[i]:
                dfs(neigh, visit)
            return len(visit)

        count = 0
        for i in range(len(bombs)):
            count = max(count, dfs(i, set()))
        return count