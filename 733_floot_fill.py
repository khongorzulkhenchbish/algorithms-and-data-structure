from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS until we reach a cell with diff val than source
        # 1. How can I pass down the source color? - if defined outside of the DFS func, no need
        # 2. When to stop? - out of bound, already painted, we shouldn't change current cell.

        # BFS, Time: O(N), Space: O(N) because of the queue
        src_color = image[sr][sc]
        if src_color == color: # if the color is set in the source cell, no need to go forward
            return image

        rows, cols = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color # Paint the starting pixel immediately

        while q:
            r, c = q.popleft()
            # The "Double-Queue" Trap
            # In BFS, you should mark a cell as visited (or paint it) the moment you add it to the queue,
            # not when you pop it. Why?
            # If you wait until you popleft() to paint the cell, the same neighbor might be added to the
            # queue multiple times by different "parents" before it ever gets a chance to be painted.
            # In a large grid of the same color, your queue size could explode exponentially, leading to
            # a Time Limit Exceeded (TLE) or Memory error.
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == src_color:
                    # Paint BEFORE adding to queue to prevent duplicates
                    image[nr][nc] = color
                    q.append((nr, nc))
                    
        return image


        # DFS - modify in-place
        # Space: O(1) if we exclude the DFS
        # Time: O(N) at most we paint every other cells.
        def dfs(cur_r, cur_c):
            # if it's already the target color, we stop; if it's not the color we're looking to change, we stop
            if cur_r < 0 or cur_r == rows or cur_c < 0 or cur_c == cols or image[cur_r][cur_c] == color or image[cur_r][cur_c] != src_color:
                return
            
            # paint as this is originally the same color as source
            image[cur_r][cur_c] = color

            # call neighbors
            nbs = [(-1,0), (1,0), (0,-1), (0,1)]
            for r,c in nbs:
                nr = cur_r + r
                nc = cur_c + c
                dfs(nr, nc)
            
        rows, cols = len(image), len(image[0])
        src_color = image[sr][sc]
        dfs(sr, sc)
        return image
