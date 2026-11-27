class Solution:
    def pascalCase(self, arr, pat):
        result = []
        for word in arr:
            capitals = "".join(ch for ch in word if ch.isupper())
            if capitals.startswith(pat):
                result.append(word)
        return result
