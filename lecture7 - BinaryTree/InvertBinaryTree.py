from typing import Optional


#По сути отзеркалить дерево, поменять местами левое и правое поддерево
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Меняем местами левое и правое поддерево
        root.left, root.right = root.right, root.left
        # Рекурсивно инвертируем левое и правое поддерево
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
      