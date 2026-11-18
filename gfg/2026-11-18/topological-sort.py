from collections import deque


class Solution:
    def topoSort(self, adj: list[list[int]]) -> list[int]:
        n = len(adj)
        indegree = [0] * n
        for u in range(n):
            for v in adj[u]:
                indegree[v] += 1

        queue = deque(u for u in range(n) if indegree[u] == 0)
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return order
