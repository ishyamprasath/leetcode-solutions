from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for v in range(1, n):
            children[parent[v]].append(v)

        # Find the new parent of each node: its closest ancestor with the same letter.
        new_parent = parent[:]
        last = {}  # letter -> stack of ancestors on the current path
        stack = [(0, False)]
        while stack:
            node, leaving = stack.pop()
            ch = s[node]
            if leaving:
                last[ch].pop()
                continue
            if node and last.get(ch):
                new_parent[node] = last[ch][-1]
            last.setdefault(ch, []).append(node)
            stack.append((node, True))
            for c in children[node]:
                stack.append((c, False))

        # Subtree sizes in the new tree, processing children before parents.
        new_children = [[] for _ in range(n)]
        for v in range(1, n):
            new_children[new_parent[v]].append(v)
        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(new_children[node])
        size = [1] * n
        for node in reversed(order):
            if node:
                size[new_parent[node]] += size[node]
        return size
