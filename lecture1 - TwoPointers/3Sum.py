from typing import List

#nums[i] + nums[j] + nums[k] == 0

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(nlogn)
        result = set()
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum == target:
                    result.add((nums[i], nums[left], nums[right]))
                if currentSum > target:
                    right -= 1
                else:
                    left += 1
        return result
#Сложность по времени O(n^2)
#Сложность по памяти константа

s = [-1,0,1,2,-1,-4]
sol = Solution()
print(f'Array: {s}, result: {sol.threeSum(s)}')