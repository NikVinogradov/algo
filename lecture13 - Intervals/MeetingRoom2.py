from typing import List

#Сколько нужно комнат для встреч, чтобы вместить все встречи без пересечений
class Solution:
    def minMeetingRoom(self, intervals: List[List[int]]) -> int:
        р = []
        intervals.sort()  # Сортируем встречи по началу
        heappush(h, intervals[0][1])  # Добавляем первую встречу в кучу
        for i in range(1, len(intervals)):
            current = intervals[i]
            
            if current[0] >= h[0]:
                heappop(h)

            heappush(h, current[1])  # Добавляем конец текущей встречи в кучу
        return len(h)  # Количество комнат равно размеру кучи
