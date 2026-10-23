class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace("-", "").upper()
        first = len(cleaned) % k
        parts = [cleaned[:first]] if first else []
        for i in range(first, len(cleaned), k):
            parts.append(cleaned[i:i + k])
        return "-".join(parts)
