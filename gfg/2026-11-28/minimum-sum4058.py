class Solution:
    def minSum(self, arr):
        digits = sorted(arr)
        # deal digits alternately to the two numbers, smallest digits first
        a = digits[0::2]
        b = digits[1::2]
        # add the two numbers digit by digit from the right (as strings, they can be long)
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        out = []
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += a[i]
                i -= 1
            if j >= 0:
                s += b[j]
                j -= 1
            out.append(s % 10)
            carry = s // 10
        result = "".join(map(str, reversed(out))).lstrip("0")
        return result or "0"
