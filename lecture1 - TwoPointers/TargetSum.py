from typing import List

#Array is sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                return[nums[left], nums[right]]
            if currentSum > target:
                right -= 1
            else:
                left += 1
        return []
#Сложность по времени O(n)
#Сложность по памяти константа

s = [1,3,4,6,10]
sol = Solution()
target = 9
print(f'Array: {s}, target: {target}, result: {sol.twoSum(s, 9)}')