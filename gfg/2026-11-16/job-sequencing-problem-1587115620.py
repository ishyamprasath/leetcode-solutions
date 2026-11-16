import heapq


class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = sorted(zip(deadline, profit))
        chosen = []
        for d, p in jobs:
            heapq.heappush(chosen, p)
            if len(chosen) > d:
                heapq.heappop(chosen)
        return [len(chosen), sum(chosen)]
