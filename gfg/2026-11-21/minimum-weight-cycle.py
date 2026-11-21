class Solution:
    def findMinCycle(self, adj: list[list[list[int]]]) -> int:
        INF = float('inf')
        n = len(adj)
        best = INF
        w = [[INF] * n for _ in range(n)]
        edge_weights = {}
        for u in range(n):
            for v, wt in adj[u]:
                if u == v:
                    best = min(best, wt)  # self-loop
                elif u < v:
                    edge_weights.setdefault((u, v), []).append(wt)
        for (u, v), ws in edge_weights.items():
            ws.sort()
            w[u][v] = w[v][u] = ws[0]
            if len(ws) > 1:
                best = min(best, ws[0] + ws[1])  # two parallel edges
        # Floyd-Warshall that closes cycles through the newest vertex k.
        d = [row[:] for row in w]
        for i in range(n):
            d[i][i] = 0
        for k in range(n):
            for i in range(k):
                if w[i][k] == INF:
                    continue
                for j in range(i):
                    if w[k][j] != INF and d[i][j] != INF:
                        best = min(best, d[i][j] + w[i][k] + w[k][j])
            for i in range(n):
                d_ik = d[i][k]
                if d_ik == INF:
                    continue
                row_i, row_k = d[i], d[k]
                for j in range(n):
                    if d_ik + row_k[j] < row_i[j]:
                        row_i[j] = d_ik + row_k[j]
        return best if best != INF else -1
