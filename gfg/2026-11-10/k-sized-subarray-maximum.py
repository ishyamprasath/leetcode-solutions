# K Sized Subarray Maximum — GFG 160 Queue and Deque, course position 108 — https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1
from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        indices = deque()
        maxima = []

        for i, value in enumerate(arr):
            while indices and indices[0] <= i - k:
                indices.popleft()
            while indices and arr[indices[-1]] <= value:
                indices.pop()
            indices.append(i)

            if i >= k - 1:
                maxima.append(arr[indices[0]])

        return maxima
