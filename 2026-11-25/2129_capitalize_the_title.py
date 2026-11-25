class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = []
        for w in title.split():
            w = w.lower()
            words.append(w if len(w) <= 2 else w[0].upper() + w[1:])
        return " ".join(words)
