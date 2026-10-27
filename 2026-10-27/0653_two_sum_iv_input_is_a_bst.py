# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Difficulty: Easy
# Approach: DFS with a hash set of seen values, look for complement.
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if k - node.val in seen:
                return True
            seen.add(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return False
