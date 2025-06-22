from typing import List

class Solution:
    def minSubArrayLen(self, nums:List[int], k: int) -> int:
        begin = 0
        window_state = 0
        result = float('inf')

        for end in range(len(nums)):
            window_state += nums[end]


            while window_state >= k:
                window_size = end - begin + 1
                result = min(result, window_size)
                window_state -= nums[begin]
                begin += 1 #shrink window

        if result == float('inf'):
            return 0

        return result

    
#Сложность по времени O(n)
#Сложность по памяти константа

s = [2,3,1,2,4,3]
k = 7
sol = Solution()

print(sol.minSubArrayLen(s, k))