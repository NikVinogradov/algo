from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

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