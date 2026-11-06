class Solution:
    def correctBST(self, root: 'Node') -> 'Node':
        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev
            if node is None:
                return
            inorder(node.left)
            if prev is not None and prev.data > node.data:
                if first is None:
                    first = prev
                second = node
            prev = node
            inorder(node.right)

        inorder(root)
        if first is not None and second is not None:
            first.data, second.data = second.data, first.data
        return root
