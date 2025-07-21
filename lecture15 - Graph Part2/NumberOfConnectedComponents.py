from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(edges)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        number = 0

        for i in range(n):
            if i not in seen:
                number += 1
                seen.add(i)
                stack = [i]
                while stack:
                    v = stack.pop()
                    for n in graph[v]:
                        if n not in seen:
                            seen.add(n)
                            stack.append(n)

        return number