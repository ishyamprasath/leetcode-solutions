from collections import deque

class Solution:
    def checkPath(self, adj, u, v):
        # BFS from u over the adjacency list
        seen = [False] * len(adj)
        seen[u] = True
        queue = deque([u])
        while queue:
            node = queue.popleft()
            if node == v:
                return True
            for nxt in adj[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    queue.append(nxt)
        return False
