# Problem: Univalued Binary Tree
# URL: https://leetcode.com/problems/univalued-binary-tree/
# Difficulty: Easy
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        target = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != target:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
