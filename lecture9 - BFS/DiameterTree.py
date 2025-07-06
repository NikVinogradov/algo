from collections import deque
from typing import List, Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)           
            self.d = max(d, l + r)
            return max(l, r) + 1



        dfs(root)

        return self.d
       
      