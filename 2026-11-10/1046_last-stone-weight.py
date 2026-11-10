# Last Stone Weight — Easy — https://leetcode.com/problems/last-stone-weight/
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heaviest = -heapq.heappop(heap)
            next_heaviest = -heapq.heappop(heap)
            if heaviest != next_heaviest:
                heapq.heappush(heap, -(heaviest - next_heaviest))

        return -heap[0] if heap else 0
