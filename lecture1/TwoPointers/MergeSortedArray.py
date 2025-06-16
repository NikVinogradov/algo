from typing import List

class Solution:
    def merge(self, nums1:List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
        for k in range(p1,m):
            result.append(nums1[k])
        for k in range(p2,n):
            result.append(nums2[k])

        for i in range(len(result)):
            nums1[i] = result[i]
#Сложность по времени O(n)
#Сложность по памяти константа