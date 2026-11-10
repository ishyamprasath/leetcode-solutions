# Longest Subarray With Limited Pairwise Difference — GFG 160 Queue and Deque, course position 109 — https://www.geeksforgeeks.org/problems/longest-bounded-difference-subarray/1
from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        min_indices = deque()
        max_indices = deque()
        left = 0
        best_left = 0
        best_length = 0

        for right, value in enumerate(arr):
            while min_indices and arr[min_indices[-1]] > value:
                min_indices.pop()
            min_indices.append(right)

            while max_indices and arr[max_indices[-1]] < value:
                max_indices.pop()
            max_indices.append(right)

            while arr[max_indices[0]] - arr[min_indices[0]] > x:
                if min_indices[0] == left:
                    min_indices.popleft()
                if max_indices[0] == left:
                    max_indices.popleft()
                left += 1

            length = right - left + 1
            if length > best_length:
                best_left = left
                best_length = length

        return arr[best_left:best_left + best_length]
