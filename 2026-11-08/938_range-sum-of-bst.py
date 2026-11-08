# 938. Range Sum of BST (Easy)
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            total += node.val if low <= node.val <= high else 0
            stack += [node.left] if node.left is not None and node.val > low else []
            stack += [node.right] if node.right is not None and node.val < high else []
        return total
