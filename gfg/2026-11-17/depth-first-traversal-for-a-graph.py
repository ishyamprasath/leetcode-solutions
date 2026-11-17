class Solution:
    def dfs(self, adj):
        n = len(adj)
        visited = [False] * n
        res = [0]
        visited[0] = True
        stack = [(0, 0)]
        while stack:
            u, idx = stack.pop()
            while idx < len(adj[u]) and visited[adj[u][idx]]:
                idx += 1
            if idx < len(adj[u]):
                v = adj[u][idx]
                stack.append((u, idx + 1))
                visited[v] = True
                res.append(v)
                stack.append((v, 0))
        return res
