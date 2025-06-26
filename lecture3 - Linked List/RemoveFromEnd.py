from collections import defaultdict
from typing import Optional

нужно 2 указателя при этом быстрому указателю дать преимущество
в n тогда когда первый дойдет до конца у второго будет озможность удаления


class Solution:
    def removeNFromEnd(self, head:Optional[ListNode], n:int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

    O(n) и O(1)
