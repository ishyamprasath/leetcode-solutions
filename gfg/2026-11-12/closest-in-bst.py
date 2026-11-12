class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        best = float("inf")
        node = root
        while node:
            best = min(best, abs(node.data - k))
            if best == 0:
                break
            node = node.left if k < node.data else node.right
        return best
