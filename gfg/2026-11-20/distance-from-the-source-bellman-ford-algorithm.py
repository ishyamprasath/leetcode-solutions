class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        INF = 10**8
        dist = [INF] * V
        dist[src] = 0
        # Relax every edge V - 1 times.
        for _ in range(V - 1):
            changed = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:
                break
        # One more pass: any improvement means a negative cycle.
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]
        return dist
