from collections import deque

class Solution:
    def findOrder(self, words: list[str]) -> str:
        letters = set()
        for w in words:
            letters.update(w)
        adj = {ch: set() for ch in letters}
        indeg = {ch: 0 for ch in letters}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in adj[x]:
                        adj[x].add(y)
                        indeg[y] += 1
                    break
            else:
                # No differing letter: the longer word must not come first.
                if len(a) > len(b):
                    return ""
        queue = deque(ch for ch in letters if indeg[ch] == 0)
        order = []
        while queue:
            ch = queue.popleft()
            order.append(ch)
            for nxt in adj[ch]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)
        return "".join(order) if len(order) == len(letters) else ""
