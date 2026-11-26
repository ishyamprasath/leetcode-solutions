class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(token: str) -> bool:
            if any(ch.isdigit() for ch in token):
                return False
            if token.count("-") > 1:
                return False
            punct = sum(ch in "!.," for ch in token)
            if punct > 1 or (punct == 1 and token[-1] not in "!.,"):
                return False
            if "-" in token:
                i = token.index("-")
                if i == 0 or i == len(token) - 1:
                    return False
                if not (token[i - 1].isalpha() and token[i + 1].isalpha()):
                    return False
            return True

        return sum(valid(t) for t in sentence.split())
