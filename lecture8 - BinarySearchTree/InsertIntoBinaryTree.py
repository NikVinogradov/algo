from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
       
        if val < root.value:
           root.left = self.insertIntoBST(root.left, val)
        else:
           root.right = self.insertIntoBST(root.right, val)
        
        return root
    
       
      