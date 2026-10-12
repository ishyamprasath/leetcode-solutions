class Solution:
    def findMajority(self, arr):
        # Extended Boyer-Moore voting with two candidates, then verify counts.
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0
        for x in arr:
            if x == cand1:
                cnt1 += 1
            elif x == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = x, 1
            elif cnt2 == 0:
                cand2, cnt2 = x, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        limit = len(arr) // 3
        result = []
        for c in (cand1, cand2):
            if c is not None and arr.count(c) > limit:
                result.append(c)
        return sorted(result)
