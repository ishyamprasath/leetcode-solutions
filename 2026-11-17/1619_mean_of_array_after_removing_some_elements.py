class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        cut = len(arr) // 20
        kept = arr[cut:len(arr) - cut]
        return sum(kept) / len(kept)
