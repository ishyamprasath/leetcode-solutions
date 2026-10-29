# 3841. Palindromic Path Queries in a Tree
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
# Difficulty: Hard
# Approach: P(x) = xor of char bitmasks on root->x path. Path mask(u,v) =
# P(u) ^ P(v) ^ bit(lca). Changing s[x] xors delta into P of x's whole subtree
# -> Euler tour + Fenwick (range xor update, point query). Palindrome iff
# mask has <= 1 set bit. LCA via binary lifting. O((n+q) log n).
from typing import List


class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        val = [1 << (ord(c) - 97) for c in s]
        LOG = max(1, n.bit_length())
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n  # initial prefix xor
        # iterative DFS
        seen = [False] * n
        seen[0] = True
        base[0] = val[0]
        stack = [(0, 0)]
        t = 0
        while stack:
            x, i = stack.pop()
            if i == 0:
                tin[x] = t
                t += 1
            if i < len(adj[x]):
                stack.append((x, i + 1))
                y = adj[x][i]
                if not seen[y]:
                    seen[y] = True
                    parent[y] = x
                    depth[y] = depth[x] + 1
                    base[y] = base[x] ^ val[y]
                    stack.append((y, 0))
            else:
                tout[x] = t  # subtree occupies [tin, tout)
        up = [parent]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            d = depth[a] - depth[b]
            k = 0
            while d:
                if d & 1:
                    a = up[k][a]
                d >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a, b = up[k][a], up[k][b]
            return parent[a]

        bit = [0] * (n + 1)

        def upd(i: int, x: int) -> None:  # point xor at index i (0-based)
            i += 1
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def qry(i: int) -> int:  # prefix xor [0..i]
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def pref(x: int) -> int:
            return base[x] ^ qry(tin[x])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                nv = 1 << (ord(parts[2]) - 97)
                delta = val[u] ^ nv
                if delta:
                    val[u] = nv
                    upd(tin[u], delta)
                    if tout[u] < n:
                        upd(tout[u], delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                m = pref(u) ^ pref(v) ^ val[lca(u, v)]
                ans.append(m & (m - 1) == 0)
        return ans
