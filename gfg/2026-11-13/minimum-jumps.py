class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + arr[i])
            if i == current_end:
                if farthest <= i:
                    return -1
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    return jumps
        return jumps if current_end >= n - 1 else -1
