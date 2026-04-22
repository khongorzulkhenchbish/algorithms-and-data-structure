from collections import deque
from typing import List


def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    -1: can't traverse, skip if this is the neighbor
    0: treasure, start from here calc the distances. these cells are immutable
    INF: not assigned, these cells needs update. also overwrite if there is smaller value

    Queue + multi-source BFS to start the distance calculation all at once.
    Where to stop? go until the current dist >= other source's path.
    else, update the neighbors distance.

    If there is no treasure or no more traversal cells, stop

    Time: O(R*C) each cell is enqueued and dequeued once with k=4 constant time.
    It stops when it sees the cells can't be more minimized.
    Space: O(R*C) stores everything in the worst case. No extra space due to overwriting of the rooms
    array. 
    """

    # optional handling of edge case
    if not rooms or not rooms[0]: return


    rows = len(rooms)
    cols = len(rooms[0])
    queue = deque()
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # init queue with treasure positions
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        size = len(queue) # differs by level

        for _ in range(size):
            r, c = queue.popleft()

            for x, y in neighbors:
                nr = r + x
                nc = c + y

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or rooms[nr][nc] in (0,-1):
                    # do nothing
                    continue
                
                if rooms[nr][nc] <= rooms[r][c] + 1:
                    continue
                
                # set curr min dist
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))

    """
    ex 1: [-1,-1,-1] or [inf, inf, inf] count_treasure = 0, queue = [], returns the same array
    ex 2: [0, -1, inf] count_treasure = 1, queue = [(0,0)], returns the same array
    ex 3: [0, 27., 27., 27., 0, 27.], count_treasure = 2,
          queue = [(0,0), (0,4)], [0, 0, 27., 0, 0, 0]
          queue = [(0,2), (0,3), (0,5)], [0, 1, 2, 1, 0, 1] => returns this array
    ex 4: [0, 27., 27., -1, 0, 27.], count_treasure = 2,
          queue = [(0,0), (0,4)], [0, 0, 27., 0, 0, 0]
          queue = [(0,2), (0,5)], [0, 1, 2, -1, 0, 1] => returns this array
    """
