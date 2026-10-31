class Solution:
    def mirror(self, root):
        # Iteratively swap the children of every node (avoids recursion limits).
        if root is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
