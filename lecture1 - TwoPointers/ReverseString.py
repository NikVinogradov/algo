from typing import List

class Solution:
    def reverseString(self, s:List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return
    
#Сложность по времени O(n)
#Сложность по памяти константа

s = list('Hello World!')
sol = Solution()
sol.reverseString(s)
print(''.join(s))