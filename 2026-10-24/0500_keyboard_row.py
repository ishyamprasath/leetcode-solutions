class Solution:
    def findWords(self, words: List[str]) -> List[str]: return [w for w in words if any(set(w.lower())<=set(r) for r in ("qwertyuiop","asdfghjkl","zxcvbnm"))]
