class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ''' This problem consists of two subproblem.
        994. Rotting Oranges + 778. Swim in a Rising Water
        '''
        # Part 1. Running multi-source BFS on the matrix creates "safety map"
        # which we can decide later to travel.
        thieves = deque()
        n = len(grid)

        # 1. register thieves locations
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    thieves.append((r, c))

        # 2. create initial safety map, add thieves. Space: O(N) for safe_map
        safe_map = [[0 if grid[r][c] else -1 for c in range(n)] for r in range(n)]


        # 3. run multi-source BFS
        while thieves:
            for _ in range(len(thieves)):
                x,y = thieves.popleft() # popping from the left ensures level traversal order

                # set neighbors distances
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx, yy = x+dx, y+dy
                    # inside the border
                    if 0 <= xx < n and 0 <= yy < n:
                        # it means unvisited cell found
                        if safe_map[xx][yy] == -1:
                            safe_map[xx][yy] = safe_map[x][y] + 1
                            thieves.append((xx, yy))
        # print(safe_map)
        # [0,0,0,1]     [3, 2, 1, 0]
        # [0,0,0,0]     [2, 3, 2, 1]
        # [0,0,0,0]     [2, 3, 2, 1]
        # [1,0,0,0]     [0, 1, 2, 3]

        # Part 2. Dijkstra algorithm (Greedy strategy): "BFS + minHeap"
        # We have to find max possible path between (0,0) to (n-1,n-1) such that
        # the max height across path is minimal. We are not searching for shortest path here.
        # We want to explore the cell that currently offers the highest safety. => max heap
        # Therefore, modified Dijkstra. Time: O(n^2 * LogN)
        visited = [[False for c in range(n)] for r in range(n)] # Space: O(N)

        # Heap stores: (-safety_at_this_point, r, c) Space: O(n^2) in the worst case
        maxH = [(-safe_map[0][0], 0, 0)]
        visited[0][0] = True

        while maxH:
            neg_dist, r, c = heapq.heappop(maxH) # LogN
            dist = -neg_dist # turn positive back for calculation

            # base condition - dist should be the min value already
            if r == n-1 and c == n-1:
                return dist
            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and not visited[nr][nc]):
                    visited[nr][nc] = True
                    # update the safety score (we take the lowest)
                    heapq.heappush(maxH, (-min(dist, safe_map[nr][nc]), nr, nc)) # LogN

        # Edge case
        # 1,0 => 0,1 => answer=1
        # 0,1    1,0