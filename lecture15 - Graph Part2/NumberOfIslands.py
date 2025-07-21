from collections import defaultdict, deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        number = 0
        n = len(grid)
        m = len(grid[0])

        def is_not_valid(r,c):
            return r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != '1'

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    number += 1

                    queue = deque([i, j])
                    while queue:
                        r, c = queue.popleft()
                        if not is_not_valid(r, c):           
                            grid[r][c] = '0'
                            queue.append((r + 1, c))
                            queue.append((r - 1, c))
                            queue.append((r, c + 1))
                            queue.append((r, c - 1))
        return number

