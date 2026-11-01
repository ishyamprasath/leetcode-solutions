'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def countAllPaths(self, root, k):
        count = 0
        prefix = {0: 1}
        stack = [(root, 0, False)]
        while stack:
            node, total, leaving = stack.pop()
            if leaving:
                prefix[total] -= 1
                continue
            total += node.data
            count += prefix.get(total - k, 0)
            prefix[total] = prefix.get(total, 0) + 1
            stack.append((node, total, True))
            if node.right:
                stack.append((node.right, total, False))
            if node.left:
                stack.append((node.left, total, False))
        return count
