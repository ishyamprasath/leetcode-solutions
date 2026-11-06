class Solution:
    def serialize(self, root):
        arr = []

        def pre(node):
            if node is None:
                arr.append(-1)
                return
            arr.append(node.data)
            pre(node.left)
            pre(node.right)

        pre(root)
        return arr

    def deSerialize(self, arr):
        it = iter(arr)

        def build():
            val = next(it)
            if val == -1:
                return None
            node = Node(val)
            node.left = build()
            node.right = build()
            return node

        return build()
