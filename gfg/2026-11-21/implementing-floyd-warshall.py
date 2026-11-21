class Solution:
    def floydWarshall(self, dist):
        INF = 10**8
        n = len(dist)
        for k in range(n):
            row_k = dist[k]
            for i in range(n):
                row_i = dist[i]
                d_ik = row_i[k]
                if d_ik == INF:
                    continue
                for j in range(n):
                    if row_k[j] != INF and d_ik + row_k[j] < row_i[j]:
                        row_i[j] = d_ik + row_k[j]
        return dist
