class Solution:
    def isPalinSent(self, s):
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        return cleaned == cleaned[::-1]
