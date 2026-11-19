import heapq


class Solution:
    def dijkstra(self, adj: list[list[list[int]]], src: int) -> list[int]:
        INF = float('inf')
        dist = [INF] * len(adj)
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, wt in adj[u]:
                nd = d + wt
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return dist
