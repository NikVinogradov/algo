from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            current = intervals[i]

            if current[0] < prev[1]:
                return False
            
        return True
