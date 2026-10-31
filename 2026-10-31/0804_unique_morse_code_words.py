from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                 ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                 "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({"".join(codes[ord(c) - 97] for c in w) for w in words})
