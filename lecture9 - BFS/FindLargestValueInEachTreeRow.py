from collections import deque
from typing import List, Optional


class Solution:
    def largestValue(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        q = deque([root])
        while q:
            level_size = len(q)
            level_max = float('-inf')

            for _ in range(level_size):
                node = q.popleft()
                level_max = max(level_max, node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)                
            result.append(level_max)
        return result
       
      