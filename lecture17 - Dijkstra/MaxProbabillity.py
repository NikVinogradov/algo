from collections import defaultdict, deque
from heapq import heappush
from typing import List


class Solution:
    def networkDelayTime(self, n:int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))


        max_heap = [(-1.0, start_node)]
        probs = {}
        probs[start_node] = 1.0

        while max_heap:
            p, node = max_heap.pop(0)

            if node == end_node:
                return -p

            for ngh, p_to_ngh in graph[node]:
                new_p = -p * p_to_ngh
                if ngh not in max_heap or new_p > probs(ngh):
                    probs[ngh] = new_p
                    heappush(max_heap, (-new_p, ngh))

        return 0  