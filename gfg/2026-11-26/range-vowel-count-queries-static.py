class Solution:
    def countVowels(self, s, queries):
        vowels = set("aeiouAEIOU")
        # prefix[i] = number of vowels in s[0:i]
        prefix = [0] * (len(s) + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (1 if ch in vowels else 0)
        return [prefix[r + 1] - prefix[l] for l, r in queries]
