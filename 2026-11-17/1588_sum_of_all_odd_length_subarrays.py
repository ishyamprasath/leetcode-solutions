class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i, x in enumerate(arr):
            subarrays = (i + 1) * (n - i)
            total += x * ((subarrays + 1) // 2)
        return total
