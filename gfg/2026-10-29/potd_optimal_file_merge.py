"""Optimal File Merge (GFG POTD 2026-10-29)
https://www.geeksforgeeks.org/problems/optimal-file-merge/1
Approach: min-heap, repeatedly merge two smallest files (Huffman style). O(n log n).
"""
import heapq
class Solution:
    def minComputation(self, files):
        heapq.heapify(files)
        total = 0
        while len(files) > 1:
            a = heapq.heappop(files)
            b = heapq.heappop(files)
            total += a + b
            heapq.heappush(files, a + b)
        return total
