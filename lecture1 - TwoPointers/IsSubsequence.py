from typing import List

class Solution:
    def isSubsequence(self, t:str, s: str) -> bool:
        p1 = 0
        p2 = 0
        while p1 < len(t) and p2 < len(s):
            if t[p1].lower() == s[p2].lower():
                p1 += 1
            p2 += 1
        return p1 == len(t)
    
#Сложность по времени O(n)
#Сложность по памяти константа

s = list('Hello World!')
t = "rld"
sol = Solution()
print(f'The word: {t}, is subsequence for {s}: {sol.isSubsequence(t,s)}')