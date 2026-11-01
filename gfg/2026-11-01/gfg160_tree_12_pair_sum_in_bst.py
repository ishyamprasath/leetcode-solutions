'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findTarget(self, root: 'Node', target: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if target - node.data in seen:
                return True
            seen.add(node.data)
            stack.append(node.left)
            stack.append(node.right)
        return False
