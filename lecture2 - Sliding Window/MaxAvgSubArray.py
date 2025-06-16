from typing import List

class Solution:
    def findMaxAverage(self, nums:List[int], k: int) -> float:
        begin = 0
        window_state = 0
        result = float('-inf')

        for end in range(len(nums)):
            window_state += nums[end]

            if end - begin + 1 == k:
                result = max(result, window_state)
                window_state -= nums[begin]
                begin += 1 #shrink window

        return result / k

    
#Сложность по времени O(n)
#Сложность по памяти константа

s = [1,12,-5,-6,50,3]
k = 4
sol = Solution()

print(sol.findMaxAverage(s, k))