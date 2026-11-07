class Solution:
    def isBalanced(self, s):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in pair:
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
        return not stack
