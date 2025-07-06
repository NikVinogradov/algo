from collections import deque
from typing import List, Optional


class Solution:
    def removeLeafModes(self, root: Optional[TreeNode], target: val) -> Optional[TreeNode]:
        if not root:
            return None

        # Recursively remove leaf nodes from left and right subtrees
        root.left = self.removeLeafModes(root.left, target)
        root.right = self.removeLeafModes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root
       
      