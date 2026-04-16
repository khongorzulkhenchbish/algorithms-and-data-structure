class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """ Clarifying question:
        What if there is no fresh orange at all? - return 0
        What if fresh orange is isolated and impossible to rot? - return -1
        What is the answer for case [2,1,2]? - return 1 because one of the "2"s will rot the "1"
        What if there are multiple rotten oranges? - yes, possible

        Intuition:
        Every minute the neighbors of the rotten orange cell rots.
        We shouldn't increase the minutes at each level.
        Queue + multi-source BFS.

        Time: O(R*C) because each cell is enqueued/dequeued at most once, each edge
        direction is checked constant times
        Space: O(R*C) Grid is modified in place, in the worst case, almost all cells will be stored
        """

        rows, cols = len(grid), len(grid[0])
        count_fresh = sum(1 for c in range(cols) for r in range(rows) if grid[r][c] == 1)
        minutes = 0
        q = deque()
        neighbors = ((0,1),(0,-1),(1,0),(-1,0)) # immutable


        # collect rotten locations
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        # process grid
        while q and count_fresh > 0:
            # level by level
            cur_size = len(q)

            for _ in range(cur_size):
                r, c = q.popleft()

                for x, y in neighbors:
                    nr = r + x
                    nc = c + y

                    # same as checking grid[nr][nc] in [0,2]
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue # the loop
                    
                    # make it rot + add to the queue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    count_fresh -= 1

            # "one BFS level == one minute"
            minutes += 1


        # check if there is still fresh oranges left
        if count_fresh > 0:
            return -1

        return minutes

        """ Dry run
        Ex 1: grid = [[2]], count_fresh = 0, q=[(0,0)], returns 0
        Ex 2: grid = [[1,1,1]], count_fresh = 3, q=[], returns -1
        Ex 3: grid = [[2,1,2]]
        queue = [(0,0), (0,2)], count_fresh = 1
        grid = [[2,2,2]], count_fresh = 0
        minutes = 1

        queue = [(0,1)], count_fresh = 0
        queue = [] and count_fresh = 0 => return 1
        """