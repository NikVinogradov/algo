from collections import defaultdict, deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])

        def is_not_valid(r,c):
            return r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != '1'

        max_area = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    current_area = 0
                    queue = deque([i, j])
                    grid[i,j] = 0

                    while queue:
                        r, c = queue.popleft()
                        current_area += 1

                        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                            nr, nc = r + dx, c + dy
                            if not is_not_valid(nr, nc):
                                grid[nr][nc] = 0
                                queue.append((nr, nc))

                    max_area = max(max_area, current_area)
        return max_area

