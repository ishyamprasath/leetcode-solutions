# Title: Decode the String
# URL: https://www.geeksforgeeks.org/problems/decode-the-string2444/1
# Difficulty: Medium
class Solution:
    def decodedString(self, s):
        stack = []
        current = []
        repeat = 0

        for ch in s:
            if ch.isdigit():
                repeat = repeat * 10 + int(ch)
            elif ch == '[':
                stack.append((current, repeat))
                current = []
                repeat = 0
            elif ch == ']':
                previous, count = stack.pop()
                previous.append(''.join(current) * count)
                current = previous
            else:
                current.append(ch)
        return ''.join(current)
