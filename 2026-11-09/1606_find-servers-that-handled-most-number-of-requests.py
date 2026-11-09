# Problem: Find Servers That Handled Most Number of Requests
# URL: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Difficulty: Hard
from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        handled = [0] * k
        for i, (time, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= time:
                _, server = heapq.heappop(busy)
                available.add(server)
            if not available:
                continue
            pos = available.bisect_left(i % k)
            if pos == len(available):
                pos = 0
            server = available.pop(pos)
            handled[server] += 1
            heapq.heappush(busy, (time + duration, server))
        best = max(handled)
        return [i for i, count in enumerate(handled) if count == best]
