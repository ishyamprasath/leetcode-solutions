from typing import List
from collections import Counter
import heapq

# LeetCode 3970 - Problem of the Day (2026-10-30)
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        # dist[node][run]: min cost to reach node with a trailing run of length run
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]
        while heap:
            d, u, run = heapq.heappop(heap)
            if d > dist[u][run]:
                continue
            if u == n - 1:
                return d
            for v, w in graph[u]:
                nxt = run + 1 if labels[v] == labels[u] else 1
                if nxt > k:
                    continue
                if d + w < dist[v][nxt]:
                    dist[v][nxt] = d + w
                    heapq.heappush(heap, (d + w, v, nxt))
        return -1
