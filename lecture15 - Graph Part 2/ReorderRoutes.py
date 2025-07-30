from collections import defaultdict, deque
from typing import List

#Все дороги в городе должны идти в один город
# и нужно сделать минимальное количество перестановок дорог
class Solution:
    def minReorder(self, n:int, connections: List[List[str]]) -> int:
        og_directions = set()
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            og_directions.add((a, b))  # Original direction

        turns = 0
        seen = {0}
        stack = [0]

        while stack:
            v = stack.pop()
            for n in graph[v]:
                if n not in seen:
                    seen.add(n)
                    stack.append(n)
                    if (v, n) in og_directions:
                        turns += 1

        return turns
