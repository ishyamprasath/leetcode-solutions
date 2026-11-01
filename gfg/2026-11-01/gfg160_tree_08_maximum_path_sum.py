'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findMaxSum(self, root):
        # iterative post-order to avoid recursion depth issues
        best = float('-inf')
        gain = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left = max(gain[node.left], 0) if node.left else 0
                right = max(gain[node.right], 0) if node.right else 0
                best = max(best, node.data + left + right)
                gain[node] = node.data + max(left, right)
        return best
