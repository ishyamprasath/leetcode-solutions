class Solution:
    def findLCA(self, root: 'Node', n1: 'Node', n2: 'Node') -> 'Node':
        a = n1.data
        b = n2.data
        if a > b:
            a, b = b, a
        node = root
        while node is not None:
            if node.data > b:
                node = node.left
            elif node.data < a:
                node = node.right
            else:
                return node
        return None
