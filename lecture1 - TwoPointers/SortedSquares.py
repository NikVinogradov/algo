from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums) # O(nlogn)
        result = [0] * n
        left = 0
        right = n - 1

        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right] * nums[right]
                right -= 1
            else:
                result[i] = nums[left] * nums[left]
                left += 1
        return result

#Сложность по времени O(n)
#Сложность по памяти константа

s = [-4,-1,0,3,10]
sol = Solution()
print(f'Array: {s}, result: {sol.sortedSquares(s)}')