# LeetCode 144. Binary Tree Preorder Traversal (Easy)
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
