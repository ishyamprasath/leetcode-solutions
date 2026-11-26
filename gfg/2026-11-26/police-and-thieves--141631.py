class Solution:
    def catchThieves(self, arr, k):
        police = [i for i, ch in enumerate(arr) if ch == 'P']
        thieves = [i for i, ch in enumerate(arr) if ch == 'T']
        caught = 0
        p = t = 0
        while p < len(police) and t < len(thieves):
            if abs(police[p] - thieves[t]) <= k:
                caught += 1
                p += 1
                t += 1
            elif thieves[t] < police[p]:
                t += 1
            else:
                p += 1
        return caught
