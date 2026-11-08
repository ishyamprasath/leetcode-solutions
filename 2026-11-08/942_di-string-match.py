# 942. DI String Match (Easy)
class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        lo, hi = 0, len(s)
        answer = []
        for i, ch in enumerate(s):
            answer.append(lo if ch == 'I' else hi)
            lo += ch == 'I'
            hi -= ch == 'D'
            if i == len(s) - 1: return answer + [lo]
