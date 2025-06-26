from collections import defaultdict
from typing import Optional

class Solution:
    def deleteDuplicates(self, head:Optional[ListNode]) -> bool:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    O(n) и O(1)
