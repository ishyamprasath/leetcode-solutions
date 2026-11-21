class Solution:
    def smallestSubWithSum(self, arr, x):
        n = len(arr)
        best = n + 1
        window = 0
        left = 0
        for right in range(n):
            window += arr[right]
            # Shrink from the left while the sum stays greater than x.
            while window > x:
                best = min(best, right - left + 1)
                window -= arr[left]
                left += 1
        return best if best <= n else 0
