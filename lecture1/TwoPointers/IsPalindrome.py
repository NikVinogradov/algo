from typing import List

class Solution:
    def isPalindrome(self, s:List[str]) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
#Сложность по времени O(n)
#Сложность по памяти константа

s = list('Hello World!')
sol = Solution()
print(f'The word: {s}, is palindrom: {sol.isPalindrome(s)}')

s2 = list('Ababa')
print(f'The word: {s2}, is palindrom: {sol.isPalindrome(s2)}')