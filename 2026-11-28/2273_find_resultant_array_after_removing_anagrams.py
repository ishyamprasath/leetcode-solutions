class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for w in words[1:]:
            if sorted(w) != sorted(result[-1]):
                result.append(w)
        return result
