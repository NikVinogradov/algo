from typing import List

class Solution:
    def longestSubarray(self, nums:List[int]) -> int:
        begin = 0
        window_state = 0 # how much zeros?
        result = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                window_state += 1

            while window_state > 1:
                if nums[begin] == 0:
                    window_state -= 1
                begin += 1 #shrink window

            result = max(result, end - begin + 1)
        return result - 1

    
#Сложность по времени O(n)
#Сложность по памяти константа

s = [1,1,0,1]
sol = Solution()

print(sol.longestSubarray(s))