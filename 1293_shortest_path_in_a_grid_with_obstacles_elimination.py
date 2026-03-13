class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # We should use BFS because if we use DFS, we could fall into the trap of
        # visiting the deepest path like 100 steps while the shortest path could
        # be 10 steps away from starting position.

        # It is allowed to visited a cell twice.
        # We should keep visited=(r, c, k) because there could be a case where we visit
        # a cell after breaking the obstacle, and that is different from visited=(r, c, k+1).

        # Time: O(M * N * K) as we might visit some cells k times in addition
        # Space: O(M * N * K) 
        n, m = len(grid), len(grid[0])
        visited = set()
        q = deque()
        q.append((0, 0, k, 0))
        visited.add((0, 0, k))

        while q:
            level_items = len(q)
            for _ in range(level_items):
                r, c, k, path = q.popleft()

                # base condition
                if r == n-1 and c == m-1 and k >= 0:
                    return path
                
                # if the cell is not obstacle continue
                # check the neighbors and add as children
                nbs = [(-1,0), (1,0), (0,-1), (0,1)]
                for x, y in nbs:
                    nr = r + x
                    nc = c + y
                    # if it is out of bounds or visited we should skip this direction
                    if 0 <= nr < n and 0 <= nc < m:
                        # if the cell is obstacle, then decrement k
                        new_k = k-1 if grid[nr][nc] == 1 else k

                        if new_k >= 0 and (nr, nc, new_k) not in visited:
                            # Mark a state as "visited" at the moment you
                            # PUSH it into the queue, not when you pop it
                            visited.add((nr, nc, new_k))

                            # As the next direction is valid, we should go forward
                            q.append((nr, nc, new_k, 1 + path))
        
        return -1
