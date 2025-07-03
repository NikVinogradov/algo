from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        result = 0
        while stack:
            node, depth = stack.pop()
            if not node:
                continue
            result = max(result, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
        return result