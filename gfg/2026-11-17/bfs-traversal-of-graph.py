class Solution:
    def bfs(self, adj):
        n = len(adj)
        visited = [False] * n
        visited[0] = True
        res = [0]
        i = 0
        while i < len(res):
            u = res[i]
            i += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    res.append(v)
        return res
