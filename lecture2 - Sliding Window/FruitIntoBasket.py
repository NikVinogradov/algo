from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, nums:List[int]) -> int:
        begin = 0
        window_state = defaultdict(int)
        result = 0

        for end in range(len(nums)):
            window_state[nums[end]] += 1

            while len(window_state) > 2:
                window_state[nums[begin]] -= 1
                if window_state[nums[begin]] == 0:
                    del window_state[nums[begin]]
                begin += 1 #shrink window

            result = max(result, end - begin + 1)
        return result

    
#Сложность по времени O(n)
#Сложность по памяти константа

s = [1,2,1]
sol = Solution()

print(sol.totalFruit(s))