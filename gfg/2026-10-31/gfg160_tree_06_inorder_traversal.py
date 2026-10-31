class Solution:
    def inOrder(self, root):
        result = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.data)
            node = node.right
        return result
