from collections import defaultdict
from typing import Optional

Два указателя
один идет со скоростью x а другой 2x
когда fast дойдет до конца, то slow дойдет до середины

Это называется Fast and slow pointer подход

class Solution:
    def middleNode(self, head:Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    O(n) и O(1)
