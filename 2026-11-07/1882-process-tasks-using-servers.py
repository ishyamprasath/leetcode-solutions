from typing import List
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n, m = len(servers), len(tasks)
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)
        ans = [0] * m
        t = 0

        for i in range(m):
            t = max(t, i)
            while busy and busy[0][0] <= t:
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))
            if not free:
                t = busy[0][0]
                while busy and busy[0][0] <= t:
                    ft, w, idx = heapq.heappop(busy)
                    heapq.heappush(free, (w, idx))
            w, idx = heapq.heappop(free)
            ans[i] = idx
            heapq.heappush(busy, (t + tasks[i], w, idx))
        return ans
