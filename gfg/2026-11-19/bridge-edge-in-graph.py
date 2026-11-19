from collections import deque


class Solution:
    def isBridge(self, V: int, edges: list[list[int]], c: int, d: int) -> bool:
        size = V + 1
        adj = [[] for _ in range(size)]
        skipped = False
        for u, v in edges:
            # Remove exactly one copy of the edge c-d.
            if not skipped and ((u == c and v == d) or (u == d and v == c)):
                skipped = True
                continue
            adj[u].append(v)
            adj[v].append(u)

        # The edge is a bridge if d is no longer reachable from c.
        seen = [False] * size
        seen[c] = True
        queue = deque([c])
        while queue:
            node = queue.popleft()
            if node == d:
                return False
            for nxt in adj[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    queue.append(nxt)
        return True
