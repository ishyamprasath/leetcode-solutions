class Solution:
    def boundaryTraversal(self, root):
        def is_leaf(node):
            return node.left is None and node.right is None
        if root is None:
            return []
        if is_leaf(root):
            return [root.data]
        result = [root.data]
        node = root.left
        while node and not is_leaf(node):
            result.append(node.data)
            node = node.left if node.left else node.right
        stack = [root]
        while stack:
            node = stack.pop()
            if is_leaf(node):
                result.append(node.data)
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        right_side = []
        node = root.right
        while node and not is_leaf(node):
            right_side.append(node.data)
            node = node.right if node.right else node.left
        result.extend(reversed(right_side))
        return result
