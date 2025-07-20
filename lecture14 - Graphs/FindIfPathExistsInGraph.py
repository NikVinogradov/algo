from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = {}

        seen[source] = True
        stack = [source]

        while stack:
            v = stack.pop()
            if v == destination:
                return True
            for neighbor in graph[v]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return False
        
