from collections import defaultdict
from typing import Optional

class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        
      prev = None
      current = head

      while current:
         tmp = current.next
         current,next = prev
         prev = current
         current = tmp
      return prev
    
    O(n) и O(1)
