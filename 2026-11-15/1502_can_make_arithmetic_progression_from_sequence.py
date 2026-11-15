class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        return all(arr[i + 1] - arr[i] == diff for i in range(len(arr) - 1))
