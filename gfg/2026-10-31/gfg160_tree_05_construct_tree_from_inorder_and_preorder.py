import sys
class Solution:
    def buildTree(self, inorder, preorder):
        sys.setrecursionlimit(10000)
        index_of = {value: i for i, value in enumerate(inorder)}
        self.pre_idx = 0
        def build(left, right):
            # Build the subtree covering inorder[left..right].
            if left > right:
                return None
            value = preorder[self.pre_idx]
            self.pre_idx += 1
            node = Node(value)
            mid = index_of[value]
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        return build(0, len(inorder) - 1)
