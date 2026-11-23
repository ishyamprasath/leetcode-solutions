class Solution:
    def height(self, root):
        # Iterative DFS: height counts edges, so a single node has height 0.
        if root is None:
            return 0
        best = 0
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            best = max(best, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return best
