# GFG POTD 2026-11-02: Largest Sum Cycle
class Solution:
    def largestSumCycle(self, edge):
        n = len(edge)
        state = [0] * n
        best = -1
        for s in range(n):
            if state[s] != 0:
                continue
            path = []
            u = s
            while u != -1 and state[u] == 0:
                state[u] = 1
                path.append(u)
                u = edge[u]
            if u != -1 and state[u] == 1:
                total = 0
                i = len(path) - 1
                while True:
                    total += path[i]
                    if path[i] == u:
                        break
                    i -= 1
                if total > best:
                    best = total
            for v in path:
                state[v] = 2
        return best
