'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def isBST(self, root: 'Node') -> bool:
        stack = []
        node = root
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None and node.data <= prev:
                return False
            prev = node.data
            node = node.right
        return True
