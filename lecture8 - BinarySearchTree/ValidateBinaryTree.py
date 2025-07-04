from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if not (lower < node.value < upper):
                return False
            stack.append((node.left, lower, node.value))
            stack.append((node.right, node.value, upper))
        
        return True
       
      