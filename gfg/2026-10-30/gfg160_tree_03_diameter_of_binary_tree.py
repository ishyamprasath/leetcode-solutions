class Solution:
    def diameter(self, root):
        # Diameter in edges: for every node, best path through it is
        # (height of left subtree + height of right subtree), heights in nodes.
        if root is None:
            return 0
        order = [root]
        for node in order:  # BFS order; children always come after their parent
            if node.left:
                order.append(node.left)
            if node.right:
                order.append(node.right)
        height = {None: 0}  # height in nodes, empty subtree = 0
        best = 0
        for node in reversed(order):
            left = height[node.left]
            right = height[node.right]
            best = max(best, left + right)
            height[node] = 1 + max(left, right)
        return best
