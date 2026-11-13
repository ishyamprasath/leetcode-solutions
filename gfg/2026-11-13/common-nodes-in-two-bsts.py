class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        def inorder(root):
            values = []
            stack = []
            node = root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                values.append(node.data)
                node = node.right
            return values

        a = inorder(r1)
        b = inorder(r2)
        i = j = 0
        common = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                if not common or common[-1] != a[i]:
                    common.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return common
