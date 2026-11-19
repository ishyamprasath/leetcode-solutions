class Solution:
    def articulationPoints(self, V: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        disc = [-1] * V
        low = [0] * V
        is_cut = [False] * V
        timer = 0

        for root in range(V):
            if disc[root] != -1:
                continue
            disc[root] = low[root] = timer
            timer += 1
            root_children = 0
            # Iterative DFS: (node, parent, index of next neighbour)
            stack = [(root, -1, 0)]
            while stack:
                node, parent, i = stack.pop()
                if i < len(adj[node]):
                    stack.append((node, parent, i + 1))
                    nxt = adj[node][i]
                    if nxt == parent:
                        continue
                    if disc[nxt] == -1:
                        disc[nxt] = low[nxt] = timer
                        timer += 1
                        if node == root:
                            root_children += 1
                        stack.append((nxt, node, 0))
                    else:
                        low[node] = min(low[node], disc[nxt])
                else:
                    # node is finished; update its parent
                    if parent != -1:
                        low[parent] = min(low[parent], low[node])
                        if parent != root and low[node] >= disc[parent]:
                            is_cut[parent] = True
            if root_children > 1:
                is_cut[root] = True

        result = [v for v in range(V) if is_cut[v]]
        return result if result else [-1]
