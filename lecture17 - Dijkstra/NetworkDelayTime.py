from collections import defaultdict, deque
from heapq import heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, w in times:
            graph[a].append((b, w))
        
        min_heap = [(0, k)]
        distances = {}
        distances[k] = 0

        while min_heap:
            dst, node = min_heap.pop(0)

            if dst > distances.get(node, float('inf')):
                continue

            for ngh, dist_to_ngh in graph[node]:
                new_dst = dst + dist_to_ngh
                if new_dst < distances.get(ngh, float('inf')):
                    distances[ngh] = new_dst
                    heappush(min_heap, (new_dst, ngh))

        if n != len(distances):
            return -1

        return distances[max(distances, key= lambda x: distances[x])]  