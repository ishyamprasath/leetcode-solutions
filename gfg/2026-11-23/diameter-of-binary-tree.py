class Solution:
    def diameter(self, root):
        # Post-order without recursion; depth[node] = edges to its deepest leaf.
        if root is None:
            return 0
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        depth = {}
        best = 0
        for node in reversed(order):
            left = depth[node.left] + 1 if node.left else 0
            right = depth[node.right] + 1 if node.right else 0
            best = max(best, left + right)
            depth[node] = max(left, right)
        return best
