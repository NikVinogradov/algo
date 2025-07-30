from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        e_r, e_c = entrance
        maze[e_r][e_c] = '+'
        queue = deque([(e_r, e_c, 0)])
        
        while queue:
            r, c, number = queue.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r = r + dr
                new_c = c + dc

                if 0<=new_r< rows and 0<=new_c<cols and maze[new_r][new_c] == '.':
                    if new_r == 0 or new_r == rows - 1 or new_c == 0 or new_c == cols - 1:
                        return number + 1

                queue.append((new_r, new_c, number + 1))
                maze[new_r][new_c] = '+'

        return -1

