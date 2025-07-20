from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def traverse(room):
            for neighbor in rooms[room]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    traverse(neighbor)
        
        seen = {0}
        traverse(0)
        return len(seen) == len(rooms)
        
