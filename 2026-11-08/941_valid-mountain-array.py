# 941. Valid Mountain Array (Easy)
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        peak = arr.index(max(arr))
        return 0 < peak < len(arr) - 1 and all(arr[i] < arr[i + 1] for i in range(peak)) and all(arr[i] > arr[i + 1] for i in range(peak, len(arr) - 1))
