from collections import deque


class Solution:
    def height(self, root):
        # Height in edges, computed level by level (iterative, no deep recursion)
        if root is None:
            return -1
        depth = -1
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
