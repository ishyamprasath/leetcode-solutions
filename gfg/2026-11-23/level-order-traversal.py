from collections import deque


class Solution:
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
