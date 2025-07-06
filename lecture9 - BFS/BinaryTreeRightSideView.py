from collections import deque
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        q = deque([root])
        while q:
            level_size = len(q)
            current_level = []

            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)                
            result.append(current_level[-1])
        return result
       
      