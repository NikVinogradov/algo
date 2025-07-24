from collections import defaultdict, deque
from heapq import heappush
from typing import List


class Solution:
    def findCheapestPrice(self, n:int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b,c in flights:
            graph[a].append((b, c))

        stops = {}

        min_heap = [(0, 0, src)]
        while min_heap:
            cost, depth, flight = min_heap.pop(0)

            if depth > k + 1:
                continue

            if flight == dst:
                return cost
            stops[flight] = depth

            for ngh, cost_to_ngh in graph[flight]:
                if (ngh not in stops or depth + 1 <= stops[ngh]):
                    heappush(min_heap, (cost + cost_to_ngh, depth + 1, ngh))