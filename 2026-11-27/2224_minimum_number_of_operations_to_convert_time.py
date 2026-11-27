class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def minutes(t: str) -> int:
            h, m = t.split(":")
            return int(h) * 60 + int(m)

        diff = minutes(correct) - minutes(current)
        ops = 0
        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step
        return ops
