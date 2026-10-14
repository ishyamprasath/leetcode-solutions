# GFG 160 Strings 2: Add Binary Strings
# Add from the right with a carry, then strip leading zeros.


class Solution:
    def addBinary(self, s1, s2):
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        out = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(s1[i]) - ord("0")
                i -= 1
            if j >= 0:
                total += ord(s2[j]) - ord("0")
                j -= 1
            out.append(str(total % 2))
            carry = total // 2
        result = "".join(reversed(out)).lstrip("0")
        return result or "0"
