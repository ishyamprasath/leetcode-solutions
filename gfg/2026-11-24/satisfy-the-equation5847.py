class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        # Group every pair (i, j), i < j, by its sum, kept in lexicographic order.
        # A pair is stored as one int i * n + j to save memory.
        by_sum = {}
        for i in range(n):
            ai = arr[i]
            for j in range(i + 1, n):
                s = ai + arr[j]
                lst = by_sum.get(s)
                if lst is None:
                    by_sum[s] = [i * n + j]
                else:
                    lst.append(i * n + j)

        # Walk (a, b) in lexicographic order; position of (a, b) inside its own list.
        seen = {}
        for a in range(n):
            for b in range(a + 1, n):
                s = arr[a] + arr[b]
                lst = by_sum[s]
                k = seen.get(s, 0)
                seen[s] = k + 1
                # Later pairs in this list are lexicographically larger than (a, b).
                for idx in range(k + 1, len(lst)):
                    c, d = divmod(lst[idx], n)
                    if c != a and c != b and d != a and d != b:
                        return [a, b, c, d]
        return [-1, -1, -1, -1]
