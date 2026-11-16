class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        arr = sorted(arr)
        dep = sorted(dep)
        n = len(arr)
        platforms = best = 0
        i = j = 0
        while i < n:
            if arr[i] <= dep[j]:
                platforms += 1
                best = max(best, platforms)
                i += 1
            else:
                platforms -= 1
                j += 1
        return best
