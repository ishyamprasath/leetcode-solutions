import heapq


class Solution:
    def minCost(self, arr):
        heap = list(arr)
        heapq.heapify(heap)
        total = 0
        # always join the two shortest ropes
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            total += a + b
            heapq.heappush(heap, a + b)
        return total
