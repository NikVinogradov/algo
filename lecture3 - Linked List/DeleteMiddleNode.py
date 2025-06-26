from collections import defaultdict
from typing import Optional

Два указателя
один идет со скоростью x а другой 2x
когда fast дойдет до конца, то slow дойдет до середины

Это называется Fast and slow pointer подход

Ксли дадим 2 шага форы fast указателю, то мы остановимся
за 1 шаг до середины slow указателем что даст возможность
удалить середину

class Solution:
    def deleteMiddleNode(self, head:Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None
        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
    
    O(n) и O(1)
