# At Least K Occurrences — POTD — https://www.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1
class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        counts = {}
        for value in arr:
            counts[value] = counts.get(value, 0) + 1
            if counts[value] == k:
                return value
        return -1
