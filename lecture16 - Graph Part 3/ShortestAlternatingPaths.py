from typing import List

from sklearn.base import defaultdict

#Самый короткий путь в графе с чередующимися цветами рёбер
class Solution:
    def shortestAlternatingPaths(self, n:int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(list))
        RED = 0
        BLUE = 1
        for a, b in redEdges:
            graph[RED][a].append(b)
        for a, b in blueEdges:
            graph[BLUE][a].append(b)
        
        result = [float('inf')] * n
        result[0] = 0
        queue = [(0, RED, 0), (0, BLUE, 0)]
        seen = {(0, RED), (0, BLUE)}
        while queue:
            v, color, depth = queue.popleft()
            result[v] = min(result[v], depth) if result[v] != -1 else depth
            for neighbor in graph[color][v]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1 - color))
                    queue.append((neighbor, 1 - color, depth + 1))

        return [x if x != float('inf') else -1 for x in result]

