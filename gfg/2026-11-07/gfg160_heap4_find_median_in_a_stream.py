import heapq


class Solution:
    def getMedian(self, arr):
        lo, hi = [], []  # max-heap (neg), min-heap
        out = []
        for num in arr:
            heapq.heappush(lo, -num)
            heapq.heappush(hi, -heapq.heappop(lo))
            if len(hi) > len(lo):
                heapq.heappush(lo, -heapq.heappop(hi))
            if len(lo) > len(hi):
                out.append(float(-lo[0]))
            else:
                out.append((-lo[0] + hi[0]) / 2.0)
        return out
