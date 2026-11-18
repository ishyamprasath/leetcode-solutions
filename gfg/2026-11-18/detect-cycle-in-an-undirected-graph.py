from collections import deque


class Solution:
    def isCycle(self, adj: list) -> bool:
        n = len(adj)
        parent = [-2] * n  # -2 means not visited
        for start in range(n):
            if parent[start] != -2:
                continue
            parent[start] = -1
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if parent[v] == -2:
                        parent[v] = u
                        queue.append(v)
                    elif v != parent[u]:
                        return True
        return False
