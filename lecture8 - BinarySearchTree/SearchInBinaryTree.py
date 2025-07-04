from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val) -> Optional[TreeNode]:
        if root and root.value == val:
            return root
       
        if not root:
            return root

        if val < root.value:
           return self.searchBST(root.left, val)
        else:
           return self.searchBST(root.right, val)
       
      