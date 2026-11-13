class Solution:
    def sortString(self, s: str) -> str:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - 97] += 1
        result = []
        while len(result) < len(s):
            for i in list(range(26)) + list(range(25, -1, -1)):
                if counts[i]:
                    result.append(chr(i + 97))
                    counts[i] -= 1
        return "".join(result)
