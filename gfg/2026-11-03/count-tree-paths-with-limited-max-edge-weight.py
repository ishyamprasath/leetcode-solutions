# GFG POTD 2026-11-03: Count Tree Paths With Limited Max Edge Weight
# Offline union-find: add edges by weight, answer queries in ascending order.
class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges = sorted(edges, key=lambda e: e[2])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        res = [0] * len(queries)
        pairs = 0
        j = 0
        m = len(edges)
        for qi in order:
            x = queries[qi]
            while j < m and edges[j][2] <= x:
                a = find(edges[j][0])
                b = find(edges[j][1])
                if a != b:
                    pairs += size[a] * size[b]
                    if size[a] < size[b]:
                        a, b = b, a
                    parent[b] = a
                    size[a] += size[b]
                j += 1
            res[qi] = pairs
        return res
