from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1:
            return -1
        
        grid[0][0] = 1
        queue = deque([(0, 0, 1)])
        
        while queue:
            r, c, number = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return number

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (-1,-1),(1,-1), (-1,1)]:
                new_r = r + dr
                new_c = c + dc

                if 0<=new_r< rows and 0<=new_c<cols and grid[new_r][new_c] == 0:
                    if new_r == rows - 1 and new_c == cols - 1:
                        return number + 1

                queue.append((new_r, new_c, number + 1))
                grid[new_r][new_c] = 1

        return -1

