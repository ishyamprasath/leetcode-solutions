class Solution:
    def minCost(self, houses: list[list[int]]) -> int:
        # Prim's algorithm on the complete graph (O(n^2)).
        n = len(houses)
        in_tree = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0
        total = 0
        for _ in range(n):
            u = -1
            for i in range(n):
                if not in_tree[i] and (u == -1 or dist[i] < dist[u]):
                    u = i
            in_tree[u] = True
            total += dist[u]
            ux, uy = houses[u]
            for v in range(n):
                if not in_tree[v]:
                    cost = abs(ux - houses[v][0]) + abs(uy - houses[v][1])
                    if cost < dist[v]:
                        dist[v] = cost
        return total
