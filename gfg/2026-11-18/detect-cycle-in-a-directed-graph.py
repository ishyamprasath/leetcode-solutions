from collections import deque


class Solution:
    def isCyclic(self, adj: list[list[int]]) -> bool:
        # Kahn's algorithm: a cycle exists if not every vertex gets removed
        n = len(adj)
        indegree = [0] * n
        for u in range(n):
            for v in adj[u]:
                indegree[v] += 1

        queue = deque(u for u in range(n) if indegree[u] == 0)
        removed = 0
        while queue:
            u = queue.popleft()
            removed += 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return removed != n
